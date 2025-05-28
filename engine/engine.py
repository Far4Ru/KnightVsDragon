import arcade

from engine.managers.asset_manager import AssetManager
from engine.managers.config_manager import ConfigManager
from engine.managers.font_manager import FontManager
from engine.managers.scene_manager import SceneManager
from engine.managers.sound_manager import SoundManager
from engine.managers.texture_manager import TextureManager

from config import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE


def singleton(cls):
    if not hasattr(cls, '_instance'):
        cls._instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super(self.__class__, self).__new__(self)
            self._instance._init()
        return self._instance

    cls.__new__ = __new__
    return cls


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
