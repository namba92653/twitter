import tweepy
import random


#インスタンス生成
def api():
    #APIキー
    CONSUMER_KEY = '取得したCONSUMER_KEY'
    CONSUMER_SECRET = '取得したCONSUMER_SECRET'
    ACCESS_TOKEN = '取得したACCESS_TOKEN'
    ACCESS_SECRET = '取得したACCESS_SECRET'

    auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
    return tweepy.api(auth)

def lists():
    search_results=api.search(q="ブログ", count=20)
    for result in search_results:
        tweet_id=result.id
        try:
            api.create_favorite(tweet_id)
        except:
            pass


def lists2():
    q_list=["#ブログ","#プログラミング","#python"]

    for q in q_list:
        search_results=api.search(q=q,count=10)
        for result in search_results:
            tweet_id=result.id
            try:
                api.create_favorite(tweet_id)
            except:
                pass


def tweetlist():
    #投稿
    tweets=["おはようございます","こんにちは","こんばんは"]
    api().update_status(random.choice(tweets))
