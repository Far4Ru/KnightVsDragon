import arcade
from arcade.examples.drawing_text import DEFAULT_FONT_SIZE

from engine.core.scene import Scene
from engine.engine import GameEngine
from pyglet.graphics import Batch

from game.components.menu_background import MenuBackground
from game.views.game_view import GameView


class MenuView(Scene):

    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLUE
        self.sprites = arcade.SpriteList()
        self.background = None
        self.player_sprite = None
        self.batch = Batch()
        self.rotating_text = arcade.Text(
            "Играть",
            400, 500,
            arcade.color.BLACK,
            DEFAULT_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            rotation=45,
            font_name="Foxcroft NF",
            batch=self.batch,
        )
        self.play_text = arcade.Text(
            "Продолжить",
            800,
            500,
            arcade.color.BLACK,
            18,
            rotation=-45,
            font_name="Foxcroft NF",
            batch=self.batch,
        )
        self.exit_text = arcade.Text(
            "Выйти",
            800, 100,
            arcade.color.BLACK,
            DEFAULT_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            font_name="Foxcroft NF",
            rotation=90,
            batch=self.batch,
        )

    def setup(self):
        self.background = MenuBackground(self.sprites)

        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_person/femalePerson_idle.png",
            scale=1,
        )
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.sprites.append(self.player_sprite)
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
        self.sprites.draw()
        self.batch.draw()
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            GameEngine().scene_manager.change_scene(GameView())
