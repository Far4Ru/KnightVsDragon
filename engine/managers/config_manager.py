
from engine.core.manager import manager


@manager
class ConfigManager:
    def __init__(self):
        self.configs = {}
        
    def add(self, filename, json_object):
        self.configs[filename] = json_object
    
    def get(self, filename):
        return self.configs[filename]
