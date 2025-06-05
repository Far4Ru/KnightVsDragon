import arcade

from engine.core.object_factory import ObjectFactory
from engine.core.scene import Scene
from engine.managers import AssetManager, ConfigManager, FontManager, SceneManager, SoundManager, TextureManager

from config import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from engine.managers.animation_manager import AnimationManager
from engine.managers.settings_manager import SettingsManager
from engine.utils.singleton import singleton


@singleton
class GameEngine:
    def _init(self):
        self.scene_manager = SceneManager(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.config_manager = ConfigManager()
        self.font_manager = FontManager()
        self.texture_manager = TextureManager()
        self.sound_manager = SoundManager()
        self.animation_manager = AnimationManager()
        self.settings_manager = SettingsManager()
        self.asset_manager = AssetManager(self.texture_manager, self.config_manager, self.sound_manager,
                                          self.font_manager, self.animation_manager)
        self.add = ObjectFactory(self.texture_manager)

    def change_scene(self, scene_name):
        self.scene_manager.change_scene(Scene(self.config_manager.get("scenes")[scene_name]))

    def run(self, scene_name):
        self.change_scene(scene_name)
        arcade.run()
