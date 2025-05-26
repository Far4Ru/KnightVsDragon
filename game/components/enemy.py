import arcade

from engine.engine import GameEngine


class Enemy:
    def __init__(self, sprites):
        self.sprite = arcade.Sprite(
            GameEngine().asset_manager.get_texture("dragon"),
            center_x=1280 * 0.5,
            center_y=700,
            scale=0.5,
        )
        sprites.append(self.sprite)
