import yaml

class ConfigManager:
    def __init__(self):
        self._configs = {}
        
    def load(self, config_type, path):
        with open(path) as f:
            self._configs[config_type] = yaml.safe_load(f)
    
    def get(self, config_type, key=None):
        config = self._configs.get(config_type, {})
        return config.get(key, config) if key else config