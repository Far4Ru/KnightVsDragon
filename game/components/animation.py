from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Animation:
    elapsed = 0
    active: bool = False
