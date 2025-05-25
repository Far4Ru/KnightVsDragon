import arcade

from config import SCREEN_WIDTH, SCREEN_HEIGHT
from engine.engine import GameEngine


class GameBackground:
    def __init__(self, sprites):
        level = 1
        self.sprite = arcade.Sprite(
            path_or_texture=GameEngine().asset_manager.get_texture(f"background_level_{level}"),
            center_x=SCREEN_WIDTH * 0.5,
            center_y=SCREEN_HEIGHT * 0.5,
        )
        sprites.append(self.sprite)
