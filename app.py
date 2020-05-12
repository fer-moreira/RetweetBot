from core.settings import Settings
from core.auth import Authorization
from core.retweet import Retweet
import sys, sched, time

from tweepy.error import TweepError, RateLimitError
from urllib3.exceptions import NewConnectionError, MaxRetryError, ConnectTimeoutError


def main (auth_file_dir):
    settings = Settings(auth_file_dir).parse()
    auth = Authorization(settings)
    api = auth.api()
    rt = Retweet(api, settings)
    rt.retweet_from_timeline()

if __name__ == "__main__":
    try: 
        _args = sys.argv[1:]
        main(str(_args[0]))
    except IndexError:          print("json file argument is missing.\ntry running: python app.py auth.json")
    except MaxRetryError:       print("Maximum number of connection attempts, you may be without internet")
    except KeyboardInterrupt:   print("Process interrupted by user")
    except NewConnectionError:  print("Failed to establish a new connection, Name or service not known or maybe you are disconnected")
    except ConnectTimeoutError: print("Connection with twitter api time out, check your network connection")
    except TweepError as r:     print(r)
    except RateLimitError as r: print(r)
    except: pass