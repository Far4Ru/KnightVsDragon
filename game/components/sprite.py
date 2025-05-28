from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Position:
    x: float
    y: float


@component
@dataclass
class Sprite:
    texture: str
    scale: float = 1.0

