import time

import tweepy


class TweetBot():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    def reply_result(self, twit_name):
        # TweepyでBotの情報を読み込む
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        # reply用の情報
        user_name = twit_name
        phrase = 'テストテスト'
        # reply
        try:
            api.update_status('@' + user_name + ' ' + phrase)
        except tweepy.TweepError as e:
            print(e.reason)
