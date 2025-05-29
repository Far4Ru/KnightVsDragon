from dataclasses import dataclass

import arcade

from engine.core.component import component


@component
@dataclass
class Text:
    text: str = ""
    color: arcade.color = arcade.color.BLACK
    font_size: int = 20
