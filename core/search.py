import requests, json
from core.auth import Authorization
from core.settings import Configurations

class Search (object):
    def __init__ (self):
        self.config_data = Configurations()

        try:
            self.access_token = Authorization.access_token()
            self.search_url = self.config_data.search_url()
        except:
            raise

        try:
            self.search_headers = {
                'Authorization': 'Bearer {}'.format(self.access_token)
            }
        except:
            raise

        try:
            self.search_params = {
                'q': self.config_data.query(),
                'count': self.config_data.count(),
                'result_type': self.config_data.result_type()
            }
        except: 
            raise
    
    def dump (self):
        try:
            search_resp = requests.get(self.search_url, headers=self.search_headers, params=self.search_params)
            resp_data = search_resp.content
            loaded_data = json.loads(resp_data)
            return loaded_data
        except:
            raise
