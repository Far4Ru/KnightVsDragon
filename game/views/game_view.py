import arcade

from engine.core.scene import Scene
from engine.engine import GameEngine
from pyglet.graphics import Batch


class GameView(Scene):

    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.CREAM

    def setup(self):
        pass
        # # Создание кнопок через UI менеджер
        # engine.ui_manager.add_button(
        #     "start_btn",
        #     x=100, y=200,
        #     texture="btn_start",
        #     callback=self._on_start
        # )

    def _on_start(self):
        pass
        # engine = GameEngine()
        # engine.scene_manager.switch_to(CharacterSelectView())

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        arcade.set_background_color(self.background_color)
        self.clear()
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            pass
            # self.background_color = arcade.color.RED
