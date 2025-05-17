import arcade

from engine.core.scene import Scene
from engine.engine import GameEngine


class MenuView(Scene):

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        engine = GameEngine()

        # bg_texture = engine.resource_manager.get_texture("menu_bg")
        # self.bg_sprite = arcade.Sprite(texture=bg_texture)

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
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            arcade.set_background_color(arcade.color.RED)
