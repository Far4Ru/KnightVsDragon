import arcade
from engine.core.scene import Scene
from engine.managers.drag_manager import DragManager
from game.components.enemy import Enemy
from game.components.grid import Grid
from game.components.player import Player


class GameView(Scene):
    def __init__(self):
        super().__init__()
        self.grid = Grid(8, 8)
        
        self.drag_manager = DragManager(self.grid)
        
        self.sprites = arcade.SpriteList()
        self.player = Player(self.sprites)
        self.enemy = Enemy(self.sprites)

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

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            # GameEngine().scene_manager.change_scene(MenuView())
            pass
