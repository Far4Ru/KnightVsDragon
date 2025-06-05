from dataclasses import dataclass

from engine.core.component import component
from engine.utils.math import hex_to_rgb


@component
@dataclass
class Text:
    def __init__(self, text: str = "", color="#000000", font_size: int = 20, fulltext: str = "", width=None,
                 multiline=False, anchor_x="center", anchor_y="center"):
        self.text = text
        self.fulltext = fulltext
        self.color = hex_to_rgb(color)
        self.font_size = font_size
        self.width = width
        self.multiline = multiline
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
