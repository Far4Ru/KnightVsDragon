from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class TurnIndicator:
    duration: int = 1
