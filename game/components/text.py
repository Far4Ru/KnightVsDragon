from dataclasses import dataclass

from engine.core.component import component
from engine.utils.math import hex_to_rgb


@component
@dataclass
class Text:
    def __init__(self, text: str = "", color="#000000", font_size: int = 20):
        self.text = text
        self.color = hex_to_rgb(color)
        self.font_size = font_size
