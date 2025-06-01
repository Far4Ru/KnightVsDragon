from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Tile:
    x: int = 0
    y: int = 0
