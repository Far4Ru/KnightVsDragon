from dataclasses import dataclass
from typing import Callable

import arcade

from engine.core.component import component
from engine.engine import GameEngine
from game.views.game_view import GameView


def action_exit():
    arcade.exit()


def action_change_to_game_view():
    GameEngine().scene_manager.change_scene(GameView())


ACTIONS = {
    "exit": action_exit
}


@component
@dataclass
class Action:
    def __init__(self, action=None):
        func_name = action["name"]
        args = action.get("args", [])

        if func_name in ACTIONS:
            self.action = lambda: ACTIONS[func_name](*args)
    execute: Callable[[], None]
