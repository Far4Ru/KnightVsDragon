from dataclasses import dataclass
from typing import Callable

import arcade

from engine.core.component import component
from engine.engine import GameEngine


def action_exit():
    arcade.exit()


def action_change_to_game_view():
    # GameEngine().scene_manager.change_scene(GameView())
    pass


ACTIONS = {
    "exit": action_exit
}


def action(cls):
    if not hasattr(cls, 'action'):
        cls.action = None

    def __init__(self, action=None):
        func_name = action["name"]
        args = action.get("args", [])

        if func_name in ACTIONS:
            self.action = lambda: ACTIONS[func_name](*args)

    cls.__init__ = __init__
    return cls
