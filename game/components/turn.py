from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Turn:
    order: int = 0
    current: bool = False
