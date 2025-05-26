import arcade

from engine.engine import GameEngine


class Player:
    def __init__(self, sprites):
        self.sprite = arcade.Sprite(
            GameEngine().asset_manager.get_texture("knight"),
            center_x=1280 * 0.5,
            center_y=100,
        )
        sprites.append(self.sprite)
