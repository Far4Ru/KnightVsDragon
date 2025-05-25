import arcade

from engine.managers.asset_manager import AssetManager
from engine.managers.scene_manager import SceneManager


class GameEngine:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_engine()
        return cls._instance
    
    def _init_engine(self):
        self.scene_manager = SceneManager()
        self.asset_manager = AssetManager()
        # self.audio_manager = AudioManager()
        
    def run(self, start_scene):
        self.scene_manager.change_scene(start_scene)
        arcade.run()
