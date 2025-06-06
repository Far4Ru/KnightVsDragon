from dataclasses import dataclass

from engine.core.component import component
from game.utils.animation import animation


@animation
@component
@dataclass
class Animation:
    elapsed = 0
    duration = 1
    active: bool = False
    dt = 0

    def skip(self):
        self.elapsed = self.duration
