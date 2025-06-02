import math
import random
from engine.core.entity import Entity
from engine.core.system import system, System
from engine.utils.math import calculate_bezier
from game.components.angle import Angle
from game.components.animation_bezier import AnimationBezier
from game.components.layer import Layer
from game.components.position import Position
from game.components.scale import Scale
from game.components.sprite import Sprite

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

animation_layer_level = 5

@system
class AnimationSystem(System):
    animations = []
    def start(self, entities):
        def wrapper(context):
            def animation_add(event):
                animation_sprite = Entity("none")
                animation_sprite.add_component(Sprite(texture="sword"))
                animation_sprite.add_component(Position(x=event["start"][0], y=event["start"][1]))
                animation_sprite.add_component(Scale(scale=1))
                animation_sprite.add_component(Angle(degree=0))
                animation_sprite.add_component(Layer(level=animation_layer_level))
                entities.append(animation_sprite)
                animation = AnimationBezier(event["start"],event["end"], event["middle"], 0.3, 3)
                animation.target = animation_sprite
                context.animations.append(animation)
            return animation_add
        
        animation_callback = wrapper(self)

        self.event_bus.subscribe("animation_add", self, animation_callback)

    def on_update(self, entities, dt):
        for animation in self.animations:
            animation.elapsed += dt
            t = min(animation.elapsed / animation.duration, 1.0)
            entity = animation.target
            if entity is not None:
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
                if entity is not None:
                    entities.remove(entity)
                    entity = None
                self.animations.remove(animation)
