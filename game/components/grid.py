import arcade
from dataclasses import dataclass

from engine.core.component import component
from engine.engine import GameEngine


@component
@dataclass
class Grid:
    cols: int
    rows: int
    cell_size: int
