import arcade

from engine.core.layers import Layers, LayerType
from engine.core.scene import Scene
from engine.engine import GameEngine
from game.components.grid import Grid
from game.components.health_bar import HealthBar


class GameView(Scene):
    def __init__(self):
        super().__init__()
        # self.grid = Grid(8, 8)

        # sprites_data = [
        #     GameEngine().texture_manager.get("sword"),
        #     ":resources:images/tiles/grassMid.png",
        # ]

        # for i, texture_path in enumerate(sprites_data):
        #     sprite = arcade.Sprite(texture_path, scale=0.5)
        #     sprite.center_x = 1280 * 0.5 + 150 + i * 100
        #     sprite.center_y = 100
        #     self.layers.add("sword", sprite)

        # TODO: level system?

        # TODO: Move to drag system?
        # self.drag_manager = DragManager(self.grid, self.layers.get("sword"))

        # TODO: Turn system?
        # TODO: Sun with angle (left to right edge)
        # TODO: Add background with random clouds (moving)
        # TODO: Add sun enter sound
        # TODO: Moon with angle (left to right edge)
        # TODO: Add background with random stars (scaling)
        # TODO: Add moon enter sound
        
        # TODO: Add text bubbles with text on config

        # TODO: Add idle animation
        # TODO: Add attack animation
        # TODO: Add hit animation
        # TODO: Add win animation
        # TODO: Add lose 
        # TODO: Add idle animation
        # TODO: Add attack animation
        # TODO: Add hit animation
        # TODO: Add win animation
        # TODO: Add lose animation

        # TODO: Add side characters

        # TODO: Add items

        # TODO: Add slots (bubbles) for items
        # TODO: Add slots (bubbles) for skills
        
        # TODO: Hp bar dependency on character attribute
        # self.hp_bar = HealthBar(1280 * 0.5, 180, 100, 80)
        # TODO: Hp bar dependency on enemy attribute
        # self.enemy_hp_bar = HealthBar(1280 * 0.5, 770, 100, 80)

        # TODO: Add settings (from menu) with sound-, sound+ and exit

        # TODO: Add level saving

        # TODO: On type devil: devil idle animation visible with bubbles on click: low dragon, low knight, previous stage, next stage
