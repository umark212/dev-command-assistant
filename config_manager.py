import json


class ConfigManager:

    def __init__(self, filename="config.json"):
        self.filename = filename   #stores config.json
        self.settings = self.load()  

    #loads and reads the settings
    def load(self):
        with open(self.filename, "r") as file:
            return json.load(file) #loads json file contents into settings

    def get(self, key):   #get() function used to see if settings like  create readme and create gitignore are true or not
        return self.settings.get(key)
