import json
import os


class SettingsManager:
    def __init__(self, config_path=".config"):
        self.configs = {}
        self.config_path = config_path
        self.load()

    def set(self, property_name, value):
        self.configs[property_name] = value
        self.save()

    def get(self, property_name):
        return self.configs[property_name]

    def load(self):
        if not os.path.exists(self.config_path):
            self.save()
        with open(self.config_path, "r", encoding="utf-8") as file:
            self.configs = json.load(file)

    def save(self):
        with open(self.config_path, "w+", encoding="utf-8") as file:
            json.dump(self.configs, file)
