from tweepy import Cursor, TweepError
import json

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

        for tweet in tweets:
            try:
                tweet.retweet()
                success = "[RETWEETED -> {ID}] '{AN} - @{ANID}' - '{TEXT}...'".format(
                    ID   = tweet.id,
                    TEXT = str(tweet.text)[:50],
                    AN   = tweet.user.name,
                    ANID = tweet.user.screen_name
                )
                print(success)

            except TweepError as e:
                reason = str(e.reason).replace("'",'"')
                error = json.loads(reason)[0]
                
                print("[{STATUS}] - {ID} -> {MESSAGE}".format(
                    STATUS=error.get('code'),
                    ID=tweet.id,
                    MESSAGE=error.get('message')
                ))
            except Exception as e:
                print(e)