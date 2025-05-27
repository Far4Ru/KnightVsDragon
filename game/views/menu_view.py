import arcade

from engine.core.scene import Scene
from engine.engine import GameEngine
from pyglet.graphics import Batch

from game.components.logo import Logo
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

        # TODO: Add backround music

        # TODO: Add path lightning on hover
        # TODO: Add path darkening on disabled
        self.button_continue = MenuButton(self.batch, "Продолжить", x=800, y=600, width=100, height=20, angle=-30)
        self.play_button = MenuButton(self.batch, "Играть", x=450, y=540, width=100, height=20, angle=20)
        self.exit_text = MenuButton(self.batch, "Выйти", x=600, y=150, width=100, height=20, angle=90)
        
        # TODO: Add path arrows to background
        self.background = MenuBackground(self.sprites)
        
        # TODO: Add animation from top to final position
        self.logo = Logo(self.sprites)

        # TODO: Add animated (looped) idle knight on the left
        # TODO: Add animated (looped) idle dragon on the right

        # TODO: Add settings button (sprite with text)
        # TODO: Add settings animation on mouse enter and leave: fullfilled
        # TODO: On settings click: bubbles with options (sound-, sound+)

        # TODO: On close: add background transition
        # TODO: On close: add character active animation and transition

        # Route: menu -> dialog1 -> level1 -> dialog2 -> level2 -> ... -> dialog6 -> win
        # Lose route: menu -> dialog1 -> level1 -> lose (restart)
        # Continue: menu (continue) -> dialog3 -> level3 -> ...
        # dialog -> menu
        # level -> menu


    def on_mouse_press(self, x, y, button, modifiers):
        if self.play_button.collides_with_point(x, y):
            GameEngine().scene_manager.change_scene(GameView())

    def update(self):
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.play_button.on_mouse_motion(x, y)
        self.button_continue.on_mouse_motion(x, y)
        self.exit_text.on_mouse_motion(x, y)

    def on_draw(self):
        self.clear()
        self.sprites.draw()
        self.batch.draw()
