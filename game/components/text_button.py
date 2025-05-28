from dataclasses import dataclass
from typing import Callable, Optional

import arcade

from engine.core.component import component


def button_press_exit():
    arcade.exit()


BUTTON_ACTIONS = {
    "exit": button_press_exit
}


@component
@dataclass
class TextButton:
    text: str = ""
    x: float = 0
    y: float = 0
    width: float = 200
    height: float = 50
    color: arcade.color = arcade.color.BLACK
    font_size: int = 20


@component
@dataclass
class Angle:
    degree: int = 0


@component
@dataclass
class Clickable:
    def __init__(self, action=None):
        func_name = action["name"]
        args = action.get("args", [])

        if func_name in BUTTON_ACTIONS:
            self.on_click = lambda: BUTTON_ACTIONS[func_name](*args)
    on_click: Callable[[], None]


@component
@dataclass
class ButtonState:
    is_hovered: bool = False
    normal_color: arcade.color = arcade.color.GRAY
    hover_color: arcade.color = arcade.color.BLUE


@component
@dataclass
class ButtonSound:
    click_sound: arcade.Sound


@component
@dataclass
class Action:
    execute: Callable[[], None]
