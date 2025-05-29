from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Scale:
    scale: float = 1
