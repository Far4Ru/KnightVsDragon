import math
import random
from engine.core.system import system, System
from engine.utils.math import calculate_bezier
from game.components.angle import Angle
from game.components.animation_bezier import AnimationBezier
from game.components.position import Position
from game.components.scale import Scale

class ScaleCurves:
    @staticmethod
    def pulse(t):
        """1 → 1.5 → 1"""
        if t < 0.5:
            return 1 + t
        return 1.5 - (t - 0.5)
    
    @staticmethod
    def grow(t):
        """0.5 → 1.5"""
        return 0.5 + t
    
    @staticmethod
    def shrink(t):
        """1.5 → 0.5"""
        return 1.5 - t


@system
class AnimationSystem(System):
    animations = []
    def start(self, entities):
        self.animations.append(AnimationBezier([125, 180],[640, 700], [150,50], 0.3, 3))

    def on_update(self, entities, dt):
        for animation in self.animations:
            animation.elapsed += dt
            t = min(animation.elapsed / animation.duration, 1.0)
            for entity in entities:
                if entity.type == "test_sword":
                    position = entity.get_component(Position)
                    angle = entity.get_component(Angle)
                    scale = entity.get_component(Scale)

                    prev_pos = (position.x, position.y)

                    new_pos = calculate_bezier(animation.control_points, t)
                    position.x, position.y = new_pos
                    
                    scale.scale = ScaleCurves.pulse(t)
                    
                    dx = new_pos[0] - prev_pos[0]
                    dy = new_pos[1] - prev_pos[1]
                    if dx != 0 or dy != 0:
                        angle.degree = math.degrees(math.atan2(dx, dy))
            if t >= 1.0:
                animation.elapsed = 0
