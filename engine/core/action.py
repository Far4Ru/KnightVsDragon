from dataclasses import dataclass
from typing import Callable

import arcade

from engine.core.component import component
from engine.engine import GameEngine
from engine.utils.math import hex_to_rgb


def action_exit():
    arcade.exit()


def action_change_to_game_view():
    GameEngine().change_scene("game")


def action_change_color(self, hover_color, base_color):
    if self.target:
        if self.is_hovered:
            self.target.color = hex_to_rgb(hover_color)
        else:
            self.target.color = hex_to_rgb(base_color)


ACTIONS = {
    "exit": action_exit,
    "level1": action_change_to_game_view,
    "change_color": action_change_color,
}


def action(cls):
    if not hasattr(cls, 'action'):
        cls.action = None

    def __init__(self, action=None):
        func_name = action["name"]
        args = action.get("args", [])

        if func_name in ACTIONS:
            self.action = lambda: ACTIONS[func_name](self, *args)

    cls.__init__ = __init__
    return cls
