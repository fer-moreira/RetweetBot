import tweepy
from tweepy import OAuthHandler, API

class Authorization:
    def __init__ (self, settings):
        self.client_key = settings.client_key()
        self.client_secret = settings.client_secret()
        self.access_token_key = settings.access_token_key()
        self.access_token_secret = settings.access_token_secret()

    def oauth (self):
        __auth = OAuthHandler(
            self.client_key, 
            self.client_secret
        )
        
        __auth.set_access_token(
            self.access_token_key, 
            self.access_token_secret
        )

        return __auth

    def api (self):
        __oauth = self.oauth()
        __api = API(__oauth);
        return __api