import arcade

from engine.managers.asset_manager import AssetManager
from engine.managers.config_manager import ConfigManager
from engine.managers.font_manager import FontManager
from engine.managers.scene_manager import SceneManager
from engine.managers.sound_manager import SoundManager
from engine.managers.texture_manager import TextureManager


class GameEngine:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_engine()
        return cls._instance
    
    def _init_engine(self):
        self.scene_manager = SceneManager()
        self.config_manager = ConfigManager()
        self.font_manager = FontManager()
        self.texture_manager = TextureManager()
        self.sound_manager = SoundManager()
        self.asset_manager = AssetManager(self.texture_manager, self.config_manager, self.sound_manager, self.font_manager)
        
    def run(self, start_scene):
        self.scene_manager.change_scene(start_scene)
        arcade.run()
