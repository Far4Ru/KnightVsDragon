import arcade

from engine.managers import AssetManager, ConfigManager, FontManager, SceneManager, SoundManager, TextureManager

from config import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from engine.utils.singleton import singleton


@singleton
class GameEngine:
    def _init(self):
        self.scene_manager = SceneManager(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.config_manager = ConfigManager()
        self.font_manager = FontManager()
        self.texture_manager = TextureManager()
        self.sound_manager = SoundManager()
        self.asset_manager = AssetManager(self.texture_manager, self.config_manager, self.sound_manager,
                                          self.font_manager)

    def run(self, start_scene):
        self.scene_manager.change_scene(start_scene)
        arcade.run()
