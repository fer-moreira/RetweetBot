import sys
from core.settings import Settings
from core.auth import Authorization
from core.retweet import Retweet

from pprint import pprint

def main (auth_file_dir):
    settings = Settings(auth_file_dir)
    auth = Authorization(settings)
    api = auth.api()

    rt = Retweet(api, settings)
    rt.retweet_from_timeline()

if __name__ == "__main__":
    try: 
        _args = sys.argv[1:]
        main(str(_args[0]))
    except IndexError:
        print("json file argument is missing.\ntry running: python app.py auth.json")
    except KeyboardInterrupt:
        print("Process interrupted by the user")