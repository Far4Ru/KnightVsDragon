import arcade
from engine.core.scene import Scene
from engine.engine import GameEngine
from engine.managers.drag_manager import DragManager
from game.components.enemy import Enemy
from game.components.game_background import GameBackground
from game.components.grid import Grid
from game.components.health_bar import HealthBar
from game.components.player import Player


class GameView(Scene):
    def __init__(self):
        super().__init__()
        self.sound = arcade.Sound(GameEngine().asset_manager.get_sound("music_level1"), streaming=True)
        self.sound.play(loop=True)
        self.grid = Grid(8, 8)
        
        self.drag_manager = DragManager(self.grid)

        self.background_layer = arcade.SpriteList()
        self.background = GameBackground(self.background_layer)
        self.sprites = arcade.SpriteList()
        self.player = Player(self.sprites)
        self.enemy = Enemy(self.sprites)
        self.hp_bar = HealthBar(1280 * 0.5, 150, 100, 100)

    def on_draw(self):
        self.clear()
        self.background_layer.draw()
        self.grid.draw()
        self.drag_manager.draw()
        self.sprites.draw()
        self.hp_bar.draw()

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
