import arcade

from config import SCREEN_WIDTH, SCREEN_HEIGHT
from engine.engine import GameEngine


class MenuBackground:
    def __init__(self, sprites):
        self.sprite = arcade.Sprite(
            path_or_texture=GameEngine().asset_manager.get_texture("background_menu"),
            center_x=SCREEN_WIDTH * 0.5,
            center_y=SCREEN_HEIGHT * 0.5,
        )
        sprites.append(self.sprite)
