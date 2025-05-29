from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Position:
    x: float = 0.0
    y: float = 0.0
