import json



class Configurations (object):
    def __init__ (self):
        self.file = open(r'/home/fmoreira/Documents/Github/LulaBot/auth.json', 'r')
        self.config_data = json.loads(str(self.file.read()))

    def client_key(self): 
        return self.config_data.get('client_key')

    def client_secret (self): 
        return self.config_data.get('client_secret')

    def base_url (self):
        return self.config_data.get('base_url')

    def auth_url (self):
        return "{0}{1}".format(
            self.config_data.get('base_url'),
            self.config_data.get('auth_url')
        )

    def search_url (self): 
        return "{0}{1}".format(
            self.config_data.get('base_url'),
            self.config_data.get('search_url')
        )

    def query (self):
        return self.config_data.get('query')

    def count (self):
        return self.config_data.get('count')

    def result_type (self):
        return self.config_data.get('result_type')
