import json
import os

import tweepy

X_API_KEY = os.environ.get("X_API_KEY")
X_API_KEY_SECRET = os.environ.get("X_API_KEY_SECRET")
X_ACCESS_TOKEN = os.environ.get("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.environ.get("X_ACCESS_TOKEN_SECRET")
X_BEARER_TOKEN = os.environ.get("X_BEARER_TOKEN")


def get_trends(woeid):
    """
    指定された場所のトレンドを取得します。
    """

    auth = tweepy.OAuthHandler(X_API_KEY, X_API_KEY_SECRET)
    auth.set_access_token(X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # トレンド一覧取得
    trends = api.get_place_trends(woeid)
    return [trend["name"] for trend in trends[0]["trends"]]


def get_trends_mock(file_path, num_tweets=10):
    """
    モックのトレンドポストデータを読み込みます。
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tweets = json.load(f)
        return tweets[:num_tweets]
    except FileNotFoundError:
        print(f"ファイルが見つかりませんでした: {file_path}")
        return []


def post_tweet(text, tweet_id=None):
    """
    X に投稿または返信します。
    """

    try:
        client = tweepy.Client(
            bearer_token=X_BEARER_TOKEN,
            consumer_key=X_API_KEY,
            consumer_secret=X_API_KEY_SECRET,
            access_token=X_ACCESS_TOKEN,
            access_token_secret=X_ACCESS_TOKEN_SECRET,
        )
        tweet_params = {"text": text}
        if tweet_id:
            tweet_params["in_reply_to_tweet_id"] = tweet_id
        response = client.create_tweet(**tweet_params)
        print(f"X に投稿/返信しました: {response}")
        return response.data["id"]  # 投稿IDを返す
    except tweepy.TweepyException as e:
        print(f"X API エラー: {e}")
        return None
