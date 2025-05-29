from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Size:
    width: float = 200
    height: float = 50
