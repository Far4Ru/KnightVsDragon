import arcade
from arcade.examples.drawing_text import DEFAULT_FONT_SIZE

from config import FONT_DEFAULT
from engine.core.scene import Scene
from engine.engine import GameEngine
from pyglet.graphics import Batch

from game.components.menu_background import MenuBackground
from game.components.play_button import PlayButton
from game.views.game_view import GameView


class MenuView(Scene):

    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLUE
        self.sprites = arcade.SpriteList()
        self.background = None
        self.player_sprite = None
        self.batch = Batch()
        self.play_text = PlayButton(self.batch, "Продолжить", 800, 500, 100, 20, -45)
        self.play_button = PlayButton(self.batch, "Играть", 500, 500, 100, 20, 20)
        self.exit_text = PlayButton(self.batch, "Выйти", 800, 100, 100, 20, 90)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.play_button.collides_with_point((x, y)):
            GameEngine().scene_manager.change_scene(GameView())

    def setup(self):
        self.background = MenuBackground(self.sprites)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.play_button.collides_with_point((x, y)):
            self.play_button.enter()
        else:
            self.play_button.leave()
        if self.play_text.collides_with_point((x, y)):
            self.play_text.enter()
        else:
            self.play_text.leave()
        if self.exit_text.collides_with_point((x, y)):
            self.exit_text.enter()
        else:
            self.exit_text.leave()

    def on_draw(self):
        arcade.set_background_color(self.background_color)
        self.clear()
        self.sprites.draw()
        self.batch.draw()
