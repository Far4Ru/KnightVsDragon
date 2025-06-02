import math
import random
from engine.core.system import system, System
from game.components.angle import Angle
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

start_pos = (125, 180)
end_pos = (640, 700)
middle_pos = (150, 50)
middle_percent = 0.3
duration = 3
cp1 = (
    start_pos[0] + (end_pos[0] - start_pos[0]) * middle_percent,
    start_pos[1] + middle_pos[0]
)
cp2 = (
    start_pos[0] + (end_pos[0] - start_pos[0]) * (1 - middle_percent),
    start_pos[1] + middle_pos[1]
)

@system
class AnimationSystem(System):
    elapsed = 0
    control_points = [start_pos, cp1, cp2, end_pos]
    def on_update(self, entities, dt):
        self.elapsed += dt
        t = min(self.elapsed / self.duration, 1.0)
        for entity in entities:
            if entity.type == "test_sword":
                position = entity.get_component(Position)
                angle = entity.get_component(Angle)
                scale = entity.get_component(Scale)

                prev_pos = (position.x, position.y)

                new_pos = self._calculate_bezier(self.control_points, t)
                position.x, position.y = new_pos
                
                scale.scale = ScaleCurves.pulse(t)
                
                dx = new_pos[0] - prev_pos[0]
                dy = new_pos[1] - prev_pos[1]
                if dx != 0 or dy != 0:
                    angle.degree = math.degrees(math.atan2(dx, dy))
        if t >= 1.0:
            self.elapsed = 0
    

    def _calculate_bezier(self, points, t):
        n = len(points) - 1
        x, y = 0.0, 0.0
        
        for i, (px, py) in enumerate(points):
            coeff = self.bernstein_polynomial(n, i, t)
            x += px * coeff
            y += py * coeff
            
        return x, y

    def bernstein_polynomial(self, n, i, t):
        return math.comb(n, i) * (t ** i) * ((1 - t) ** (n - i))