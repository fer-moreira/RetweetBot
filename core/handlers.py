
class dicto(object):
    """ Convert dict to object

        - **parameters**::
            :param d: dict


        - ** Example: ** -
            >>> o = dicto({"foo":"bar"})
            >>> o.foo
            $ bar
        """

    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [dicto(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, dicto(b) if isinstance(b, dict) else b)

class Helper:
    @staticmethod
    def can_retweet (tweet, settings):
        try:
            metadata = dicto(tweet.metadata)

            if not "RT @" in str(tweet.text) \
            and metadata.iso_language_code  == settings.iso_language_code \
            and metadata.result_type        == settings.result_type:
                return True
            else:
                return False
        except TypeError as e:
            print(e)
            return False
        except:
            raise