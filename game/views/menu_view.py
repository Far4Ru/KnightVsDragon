import arcade

from engine.core.scene import Scene
from engine.engine import GameEngine
from pyglet.graphics import Batch

from game.components.menu_background import MenuBackground
from game.components.menu_button import MenuButton
from game.views.game_view import GameView


class MenuView(Scene):
    def __init__(self):
        super().__init__()
        self.sprites = arcade.SpriteList()
        self.background = None
        self.player_sprite = None
        self.batch = Batch()
        self.button_continue = MenuButton(self.batch, "Продолжить", x=800, y=500, width=100, height=20, angle=-45)
        self.play_button = MenuButton(self.batch, "Играть", x=500, y=500, width=100, height=20, angle=20)
        self.exit_text = MenuButton(self.batch, "Выйти", x=800, y=100, width=100, height=20, angle=90)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.play_button.collides_with_point(x, y):
            GameEngine().scene_manager.change_scene(GameView())

    def setup(self):
        self.background = MenuBackground(self.sprites)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.play_button.on_mouse_motion(x, y)
        self.button_continue.on_mouse_motion(x, y)
        self.exit_text.on_mouse_motion(x, y)

    def on_draw(self):
        self.clear()
        self.sprites.draw()
        self.batch.draw()
