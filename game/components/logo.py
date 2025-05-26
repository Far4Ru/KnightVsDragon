import arcade

from engine.engine import GameEngine


class Logo:
    def __init__(self, sprites):
        self.sprite = arcade.Sprite(
            GameEngine().asset_manager.get_texture("logo"),
            center_x=1280 * 0.5,
            center_y=850,
        )
        sprites.append(self.sprite)
