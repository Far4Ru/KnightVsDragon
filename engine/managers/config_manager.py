class ConfigManager:
    def __init__(self):
        self.configs = {}
        
    def add(self, filename, json_object):
        self.configs[filename] = json_object
    
    # TODO: fix
    def get(self, config_type, key=None):
        config = self._configs.get(config_type, {})
        return config.get(key, config) if key else config