from core.handlers import dicto
import json

class Settings:
    def __init__ (self, auth_file):
        file = open(auth_file, "r")
        content = file.read()
        self.data = json.loads(str(content))
    
    def parse (self):
        assert type(self.data) == dict, TypeError("waiting dict and get {0}".format(type(self.data)))
        return dicto(self.data)