import math

from engine.core.system import system
from engine.core.system import System
from engine.utils.math import calculate_bezier
from game.components import Angle, Scale, Turn
from game.components.animation_bezier import AnimationBezier
from game.components.position import Position
from game.components.sprite import Sprite
from game.components.turn_indicator import TurnIndicator


@system
class TurnIndicatorSystem(System):
    animations = []

    def start(self, entities):
        for entity in entities:
            if entity.has_component(TurnIndicator):
                def wrapper(context, e):
                    def animation_add():
                        animation = AnimationBezier([-400, 600], [1280 + 200, 500], [0, 300], 0.5, 60)
                        animation.target = e
                        context.animations.append(animation)
                    return animation_add

                animation_callback = wrapper(self, entity)

                self.event_bus.subscribe("turn_indicator_animation_add", self, animation_callback)
        self.event_bus.emit("turn_indicator_animation_add")

    def update(self, entities):
        pass

    def on_update(self, entities, dt):
        for animation in self.animations:
            animation.elapsed += dt
            t = min(animation.elapsed / animation.duration, 1.0)
            entity = animation.target
            if entity is not None:
                position = entity.get_component(Position)
                angle = entity.get_component(Angle)

                new_pos = calculate_bezier(animation.control_points, t)
                position.x, position.y = new_pos

                angle.degree = animation.elapsed * 3
            if t >= 1.0:
                animation.elapsed = 0
                # if entity is not None:
                #     entities.remove(entity)
                #     entity = None
                # self.animations.remove(animation)
