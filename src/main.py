import argparse
import os
from collections import defaultdict

from dotenv import load_dotenv

from lib import gemini_api, text, x_api


def main():
    """
    メイン処理。
    """

    # トレンドの取得
    japan_woeid = 23424856  # 日本のWOEID
    if args.mock:
        trends = x_api.get_trends_mock("mock/mock_trends.json")
    else:
        trends = x_api.get_trends(japan_woeid)
    if not trends:
        print("トレンドの取得に失敗しました。")
        return

    negative_trends = defaultdict(list)

    # テンプレート
    tmp_analyze_sentiment = text.read_text_file("prompt/analyze_sentiment.txt")
    tmp_analyze_complaint = text.read_text_file("prompt/analyze_complaint.txt")
    tmp_generate_x = text.read_text_file("prompt/generate_x.txt")
    tmp_generate_campfire = text.read_text_file("prompt/generate_campfire.txt")
    tmp_generate_qiita = text.read_text_file("prompt/generate_qiita.txt")
    tmp_generate_name = text.read_text_file("prompt/generate_name.txt")

    # トレンドからネガティブなものを取得
    for trend in trends:
        trend = trend["text"]
        # カテゴリ分け
        # TODO: 精度が甘いため、プロンプトを要整備
        sentiment = gemini_api.query(tmp_analyze_sentiment.replace("###TEXT###", trend))
        if sentiment and sentiment != "ポジティブ":
            negative_trends[sentiment].append(trend)
    if not negative_trends:
        print("ネガティブなトレンドは見つかりませんでした。")
        return

    # ネガティブトレンドからアイデアを考案
    for sentiment in negative_trends:
        idea = gemini_api.query(tmp_analyze_complaint.replace("###POST_TEXT###", "\n".join(negative_trends[sentiment])))
        if not idea:
            print("アイデア生成に失敗しました。")
            continue

        # アイデアを140字以内に形成する
        text_x = gemini_api.query(tmp_generate_x.replace("###SERVICE_TEXT###", idea))

        # キャンプファイアの形式にする
        text_campfire = gemini_api.query(tmp_generate_campfire.replace("###SERVICE_TEXT###", idea))
        text_campfire = text.remove_code_blocks(text_campfire)

        # qiitaの形式にする
        text_qiita = gemini_api.query(tmp_generate_qiita.replace("###SERVICE_TEXT###", idea))
        text_qiita = text.remove_code_blocks(text_qiita)

        # サービス名を考えて、ディレクトリを作成
        title = gemini_api.query(tmp_generate_name.replace("###SERVICE_TEXT###", idea))
        title = os.path.join("output", title)
        os.makedirs(title, exist_ok=True)

        # ファイルを作成
        targets = [("x.txt", text_x), ("campfire.md", text_campfire), ("README.md", text_qiita)]
        for filename, content in targets:
            with open(os.path.join(title, filename), "w", encoding="utf-8") as file:
                file.write(content)

        # x で紹介
        parent_post_id = x_api.post_tweet(text_x)
        parent_post_id = x_api.post_tweet(text_qiita[:140], parent_post_id)
        fasf = f"{title}\nhttps://github.com/Syogo-Suganoya/IdeaX/blob/main/output/{title}/README.md"
        x_api.post_tweet(fasf, parent_post_id)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description="トレンド分析とアイデア生成")
    parser.add_argument("--mock", action="store_true", help="モックデータを使用する")
    args = parser.parse_args()
    main()
