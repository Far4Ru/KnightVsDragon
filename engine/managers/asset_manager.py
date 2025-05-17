import json
import os

import arcade


class AssetManager:
    def __init__(self):
        self._pool = {}
        
    def load_texture(self, key, path):
        if key not in self._pool:
            self._pool[key] = arcade.load_texture(path)
        return self._pool[key]
    
    def load_level(self, level_id):
        path = f"assets/levels/level_{level_id}.json"
        with open(path) as f:
            return json.load(f)
