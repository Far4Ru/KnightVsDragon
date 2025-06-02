from dataclasses import dataclass
from typing import List

from engine.core.component import component

from pyglet.math import Vec2


@component
@dataclass
class AnimationBezier:
    elapsed = 0
    def __init__(self, start: List[int], end: List[int], middle: List[int], percent: float = 0.5, duration: float = 1):
        self.start_position = Vec2(start[0], start[1])
        self.end_position = Vec2(end[0], end[1])
        self.middle_position = Vec2(middle[0], middle[1])
        self.middle_percent = percent
        self.duration = duration

        control_point1 = (
            self.start_position.x + (self.end_position.x - self.start_position.x) * self.middle_percent,
            self.start_position.y + self.middle_position.x
        )
        control_point2 = (
            self.start_position.x + (self.end_position.x - self.start_position.x) * (1 - self.middle_percent),
            self.start_position.y + self.middle_position.y
        )
        self.control_points = [self.start_position, control_point1, control_point2, self.end_position]