from tweepy import Cursor, TweepError
import json, ast

class Retweet:
    def __init__ (self, api, settings):
        self.api = api
        self.count = int(settings.count())
        self.query = tuple(settings.query())

    def timeline (self):
        __cursor = Cursor(self.api.search, self.query)
        __tweets = __cursor.items(self.count)
        return __tweets
    
    def retweet_from_timeline (self):
        tweets = self.timeline()
        retweet_count = 0

        for tweet in tweets:
            try:
                if not "RT @" in str(tweet.text):
                    tweet.retweet()
                    retweet_count += 1
                    print("[RETWEETED -> {ID}] '{AN} - @{ANID}' - '{TEXT}...'".format(
                        ID   = tweet.id,
                        TEXT = str(tweet.text)[:50].replace("\n",""),
                        AN   = tweet.user.name,
                        ANID = tweet.user.screen_name
                    ))

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
            except Exception as e:
                print(e)

        print("Retweeted: {0}".format(retweet_count))