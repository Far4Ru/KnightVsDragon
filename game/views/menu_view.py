import arcade

from engine.core.scene import Scene
from engine.engine import GameEngine
from pyglet.graphics import Batch

from game.views.game_view import GameView


class MenuView(Scene):

    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLUE
        self.player_list = None
        self.player_sprite = None
        self.batch = Batch()
        self.play_text = arcade.Text(
            "Играть",
            500,
            500,
            arcade.color.BLACK,
            18,
            batch=self.batch,
        )

    def setup(self):

        # bg_texture = engine.asset_manage.get_texture("menu_bg")
        # self.bg_sprite = arcade.Sprite(texture=bg_texture)
        self.player_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_person/femalePerson_idle.png",
            scale=1,
        )
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)
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
        self.player_list.draw()
        self.batch.draw()
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            GameEngine().scene_manager.change_scene(GameView())
