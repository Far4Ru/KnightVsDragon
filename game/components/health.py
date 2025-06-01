from dataclasses import dataclass

from engine.core.component import component
from engine.utils.math import hex_to_rgb


@component
@dataclass
class Health:
    def __init__(self, max_hp=100, current_hp=100, background="#000000", border="#FFFFFF", fill="#FF0000"):
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.background = hex_to_rgb(background)
        self.border = hex_to_rgb(border)
        self.fill = hex_to_rgb(fill)
