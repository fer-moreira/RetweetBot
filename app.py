from core.settings import Settings
from core.auth import Authorization
from core.retweet import Retweet
import sys, sched, time


def main (auth_file_dir):
    settings = Settings(auth_file_dir).parse()
    auth = Authorization(settings)
    api = auth.api()

    s = sched.scheduler(time.time, time.sleep)
    s.enter(60*60, 1, retweet, (s,api,settings))
    s.run()

def retweet (s, api, settings):
    rt = Retweet(api, settings)
    rt.retweet_from_timeline()
    s.enter(60*60, 1, retweet, (s, api, settings))

if __name__ == "__main__":
    try: 
        _args = sys.argv[1:]
        main(str(_args[0]))
    except IndexError:
        print("json file argument is missing.\ntry running: python app.py auth.json")
    except KeyboardInterrupt:
        print("Process interrupted by user")