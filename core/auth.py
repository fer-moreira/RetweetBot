import requests 
from core.handlers import Handlers
from core.settings import Configurations

class Authorization:
    """ Make quick authorization calls """

    @staticmethod
    def access_token () -> str:
        try:
            config = Configurations()
            auth_url = config.auth_url()

            b64_keys = Handlers.encode_keys(
                client_key    = config.client_key(), 
                client_secret = config.client_secret()
            )

            auth_headers = {
                'Authorization': 'Basic {}'.format(b64_keys),
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            }

            auth_data = { 'grant_type': 'client_credentials' }
            auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
            access_token = auth_resp.json()['access_token']

            return access_token
        except: raise