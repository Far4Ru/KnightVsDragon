import arcade
from array import array
from arcade.gl import BufferDescription
from engine.core.scene import Scene
from .grid import Grid
from .drag_manager import DragManager


class GameView(Scene):
    def __init__(self):
        super().__init__()
        self.grid = Grid(8, 8)
        
        self.drag_manager = DragManager(self.grid)
        
        self.sprites = arcade.SpriteList()
        self.player = arcade.Sprite(
            ":resources:images/animated_characters/female_person/femalePerson_idle.png",
            center_x=1280 * 0.5,
            center_y=100,
        )
        self.sprites.append(self.player)

    def on_draw(self):
        self.clear()
        self.grid.draw()
        self.drag_manager.draw()
        self.sprites.draw()
        

    def on_mouse_press(self, x, y, button, modifiers):
        self.drag_manager.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.drag_manager.on_mouse_release(x, y, button, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.drag_manager.on_mouse_drag(x, y, dx, dy, buttons, modifiers)