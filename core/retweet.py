from tweepy import Cursor, TweepError
from core.handlers import dicto, Helper
import json, ast

class Retweet:
    def __init__ (self, api, settings):
        self.api = api
        self.count = int(settings.count)
        self.query = tuple(settings.query)
        self.settings = settings

    def timeline (self, count):
        __cursor = Cursor(self.api.search, self.query)
        __tweets = __cursor.items(count)
        return __tweets
    
    def retweet_from_timeline (self):
        tweets = self.timeline(self.count)
        retweet_count = 0

        for tweet in tweets:
            try:
                if Helper.can_retweet(tweet, self.settings):
                    tweet.retweet()
                    retweet_count += 1
                    print("[RETWEETED -> {ID}] '{AN} - @{ANID}' - '{TEXT}...'".format(
                        ID   = tweet.id,
                        TEXT = str(tweet.text)[:50].replace("\n",""),
                        AN   = tweet.user.name,
                        ANID = tweet.user.screen_name
                    ))
                else: pass
            except TweepError as e:
                reason = e.reason
                assert type(reason) == str, TypeError("Reason must be String type")
                reason_list = ast.literal_eval(reason)
                assert type(reason_list) == list, TypeError("reason_list should be list of dict")
                error = reason_list[0]
                # IF USER REACH THE LIMIT OF THE DAY 
                if error.get('code') == 185:
                    print("[{STATUS}] - {MESSAGE}".format(
                        STATUS=error.get('code'),
                        MESSAGE=error.get('message')
                    ))
                else:
                    print("[{STATUS}] - {ID} -> {MESSAGE}".format(
                        STATUS=error.get('code'),
                        ID=tweet.id,
                        MESSAGE=error.get('message')
                    ))

        remaining_count = (self.count - retweet_count)

        print("Retweeted: {0} | remaining: {1}\n".format(retweet_count, remaining_count))

        if remaining_count > 0:
            self.count = remaining_count
            self.retweet_from_timeline()
        