import json

class Settings:
    def __init__ (self, auth_file):
        file = open(auth_file, "r")
        content = file.read()
        self.data = json.loads(str(content))

    def client_key (self): return self.data.get('client_key')
    def client_secret (self): return self.data.get('client_secret')
    def access_token_key (self): return self.data.get('access_token_key')
    def access_token_secret (self): return self.data.get('access_token_secret')

    def query (self): return self.data.get('query')
    def count (self): return self.data.get('count')