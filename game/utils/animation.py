from typing import List

from pyglet.math import Vec2

from engine.utils.math import calculate_bezier
from game.components import Angle, Scale
from game.components.position import Position


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

    @staticmethod
    def push(t):
        """1 → 0.5 → 1"""
        if t < 0.5:
            return 1 - t
        return t


def animation_bezier_init(self, start: List[int], end: List[int], middle: List[int], percent: float = 0.5,
                          duration: float = 1):
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


def animation_bezier_update(self):
    self.elapsed += self.dt
    t = min(self.elapsed / self.duration, 1.0)
    entity = self.target
    if entity is not None:
        position = entity.get_component(Position)
        angle = entity.get_component(Angle)

        new_pos = calculate_bezier(animation.control_points, t)
        position.x, position.y = new_pos

        angle.degree = animation.elapsed * 3
    if t >= 1.0:
        animation.elapsed = 0


# animation.elapsed += dt
# t = min(animation.elapsed / animation.duration, 1.0)
# entity = animation.target
# if entity is not None:
#     position = entity.get_component(Position)
#     angle = entity.get_component(Angle)
#     scale = entity.get_component(Scale)
#
#     prev_pos = (position.x, position.y)
#
#     new_pos = calculate_bezier(animation.control_points, t)
#     position.x, position.y = new_pos
#
#     scale.scale = ScaleCurves.pulse(t)
#
#     dx = new_pos[0] - prev_pos[0]
#     dy = new_pos[1] - prev_pos[1]
#     if dx != 0 or dy != 0:
#         angle.degree = math.degrees(math.atan2(dx, dy))
# if t >= 1.0:
#     if entity is not None:
#         entities.remove(entity)
#         entity = None
#     self.animations.remove(animation)


def animation_button_push_init(self):
    pass


def animation_button_push_update(self):
    self.elapsed += self.dt
    t = min(self.elapsed / self.duration, 1.0)
    entity = self.target
    if entity is not None:
        scale = entity.get_component(Scale)

        scale.scale = ScaleCurves.push(t)
    if t >= 1.0:
        pass


ANIMATIONS = {
    "bezier": {
        "init": animation_bezier_init,
        "update": animation_bezier_update,
    },
    "button_push": {
        "init": animation_bezier_init,
        "update": animation_bezier_update,
    },
}


def animation(cls):
    if not hasattr(cls, 'init'):
        cls.init = None
    if not hasattr(cls, 'update'):
        cls.update = None

    def __init__(self, update=None, event=None, emit=None):
        self.event = event
        self.emit = emit
        func_name = update["name"]
        args = update.get("args", [])

        if func_name in ANIMATIONS:
            self.init = lambda: ANIMATIONS[func_name]["init"](self, *args)
            self.update = lambda: ANIMATIONS[func_name]["update"](self)

    cls.__init__ = __init__
    return cls
