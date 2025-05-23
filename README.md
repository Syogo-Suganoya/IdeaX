# 不満バスターズ - X（旧Twitter）トレンドから不満を解消するアイデア生成ツール

## 概要

「不満バスターズ」は、X（旧Twitter）のトレンドや投稿からネガティブな内容を抽出し、それをAIで解析して不満を解消するための具体的なサービスアイデアを生成するツールです。生成されたアイデアは、以下の形式で出力されます：

- **140文字以内の要約**（X向け投稿）
- **キャンプファイヤー形式の企画書**
- **Qiita形式の技術記事**

さらに、生成されたアイデアをXに投稿する機能も備えています。

## 主な機能

1. **トレンド取得**
   Xのトレンドを取得し、ネガティブなトレンドを抽出します（モックデータも使用可能）。

2. **感情分析**
   トレンドや投稿内容をAIで解析し、ポジティブかネガティブかを判定します。

3. **アイデア生成**
   ネガティブなトレンドに基づき、不満を解消するための具体的なサービスアイデアを生成します。

4. **形式変換**
   生成されたアイデアを以下の形式に変換します：
   - X向け140文字以内の投稿
   - キャンプファイヤー形式の企画書
   - Qiita形式の技術記事

5. **自動投稿**
   生成された内容をXに自動投稿します。

6. **ファイル出力**
   生成されたアイデアを指定のディレクトリに保存します。

## 使用技術

- **Python**
  プログラム全体の実装に使用。
- **Tweepy**
  X APIを利用してトレンド取得や投稿を実現。
- **Google GenAI**
  Geminiモデルを使用してプロンプトベースの生成を実行。
- **dotenv**
  環境変数の管理。

## 必要な環境

- Python 3
- 以下のPythonライブラリ：
  - `tweepy`
  - `google-genai`
  - `python-dotenv`

## インストール

1. 必要なライブラリをインストールします。

    ```bash
    pip install -r requirements.txt
    ```

2. 環境変数を設定します。`.env` ファイルを作成し、以下の内容を記載してください。

    ```env
    X_API_KEY="YOUR_X_API_KEY"
    X_API_KEY_SECRET="YOUR_X_API_KEY_SECRET"
    X_ACCESS_TOKEN="YOUR_X_ACCESS_TOKEN"
    X_ACCESS_TOKEN_SECRET="YOUR_X_ACCESS_TOKEN_SECRET"
    X_BEARER_TOKEN="YOUR_X_BEARER_TOKEN"
    GEMINI_KEY="YOUR_GEMINI_API_KEY"
    ```

## 実行方法

1. モックデータを使用して実行する場合：

    ```bash
    python src/main.py --mock
    ```

2. 実際のX APIを使用して実行する場合：

    ```bash
    python src/main.py
    ```

## ファイル構成

- `src/main.py`
  メインスクリプト。トレンド取得、感情分析、アイデア生成、投稿を実行します。
- `src/lib/`
  各種APIやユーティリティ関数を含むモジュール。
- `mock/`
  モックデータ（トレンドや投稿内容）を格納。
- `prompt/`
  AIプロンプトテンプレートを格納。
- `output/`
  生成されたアイデアの保存先。

## 注意事項

- X APIの利用規約を遵守してください。
- 生成されたアイデアは、必ずしも現実的または適切であるとは限りません。実装前に十分な検討を行ってください。

## 課題点・今後の展望
- X APIの導入
現在、X API の利用料が高額なため、十分なデータ取得が難しい状況です。
この問題は、クラウドファンディングで資金を集め次第、解消する予定です。
- トレンドのカテゴリ分け
現状では、各ツイートを個別に分析していますが、類似するツイートをまとめて集約することで、より正確なトレンド分析が可能になります。
今後は、適切なカテゴリ分けを行うためのプロンプトを整備し、分類精度の向上を目指します。
