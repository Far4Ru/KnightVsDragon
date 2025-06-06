from typing import List, Optional

from pyglet.math import Vec2

from engine.engine import GameEngine
from engine.utils.math import calculate_bezier
from game.components import Angle, Scale
from game.components.damage import Damage
from game.components.health import Health
from game.components.position import Position
from game.components.sprite import Sprite
from game.components.text import Text


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


def animation_bezier_later_init(self):
    if self.start_position and self.end_position and self.middle_position and self.middle_percent:
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
    if self.active:
        entity = self.target
        if entity is not None:
            if position := entity.get_component(Position):
                new_pos = calculate_bezier(self.control_points, t)
                position.x, position.y = new_pos
            if angle := entity.get_component(Angle):
                angle.degree = self.elapsed * 3
    if t >= 1.0:
        self.elapsed = 0
        self.active = False
        GameEngine().scene_manager.current_scene.event_bus.emit(
            self.emit,
            {"animation": self}
        )


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
    self.elapsed = 0
    self.active = True
    self.duration = 0.3


def animation_button_push_update(self):
    self.elapsed += self.dt
    t = min(self.elapsed / self.duration, 1.0)
    entity = self.target
    if entity is not None:
        scale = entity.get_component(Scale)

        scale.scale = ScaleCurves.push(t)
    if t >= 1.0:
        self.active = False


def animation_text_init(self):
    self.elapsed = 0
    self.active = True
    self.duration = 1
    if (entity := self.target) is not None:
        if text := entity.get_component(Text):
            self.duration = len(text.fulltext)


def animation_text_update(self):
    self.elapsed += self.dt
    t = min(self.elapsed / self.duration, 1.0)
    entity = self.target
    if entity is not None:
        if text := entity.get_component(Text):
            if len(text.text) < len(text.fulltext):
                text.text = text.fulltext[:len(text.text) + 1]
    if t >= 1.0:
        if text := entity.get_component(Text):
            text.text = text.fulltext
        self.elapsed = 0


def animation_change_state_init(self):
    self.elapsed = 0
    self.active = True
    self.duration = 0.1
    if (entity := self.target) is not None:
        if sprite := entity.get_component(Sprite):
            sprite.visible = not sprite.visible


def animation_change_state_update(self):
    self.elapsed += self.dt
    t = min(self.elapsed / self.duration, 1.0)
    entity = self.target
    if entity is not None:
        # if text := entity.get_component(Text):
        #     if len(text.text) < len(text.fulltext):
        #         text.text = text.fulltext[:len(text.text) + 1]
        pass
    if t >= 1.0:
        self.elapsed = 0
        self.active = False


def animation_health_change_init(self):
    self.elapsed = 0
    self.active = False
    self.duration = 1


def animation_health_change_update(self):
    self.elapsed += self.dt
    t = min(self.elapsed / self.duration, 1.0)
    entity = self.target
    if entity is not None:
        if health := entity.get_component(Health):
            if damage := entity.get_component(Damage):
                health.current_hp = round(health.last_hp - damage.value * t)
    if t >= 1.0:
        if health := entity.get_component(Health):
            if damage := entity.get_component(Damage):
                health.current_hp = health.last_hp - damage.value
                health.last_hp = health.current_hp
        GameEngine().scene_manager.current_scene.event_bus.emit(
            self.emit,
            {"animation": self}
        )
        self.active = False


def animation_delay_init(self, duration):
    self.elapsed = 0
    self.active = True
    self.duration = duration


def animation_delay_update(self):
    self.elapsed += self.dt
    t = min(self.elapsed / self.duration, 1.0)
    if t >= 1.0:
        self.elapsed = 0
        self.active = False
        GameEngine().scene_manager.current_scene.event_bus.emit(
            self.emit,
            {"animation": self}
        )


ANIMATIONS = {
    "bezier": {
        "init": animation_bezier_init,
        "update": animation_bezier_update,
    },
    "bezier_later": {
        "init": animation_bezier_later_init,
        "update": animation_bezier_update,
    },
    "button_push": {
        "init": animation_button_push_init,
        "update": animation_button_push_update,
    },
    "text_animation": {
        "init": animation_text_init,
        "update": animation_text_update,
    },
    "change_state": {
        "init": animation_change_state_init,
        "update": animation_change_state_update,
    },
    "health_change": {
        "init": animation_health_change_init,
        "update": animation_health_change_update,
    },
    "delay": {
        "init": animation_delay_init,
        "update": animation_delay_update,
    }
}


def animation(cls):
    if not hasattr(cls, 'init'):
        cls.init = None
    if not hasattr(cls, 'update'):
        cls.update = None
    cls.start_position = None
    cls.end_position = None
    cls.middle_position = None
    cls.middle_percent = None

    def __init__(self, update=None, event: Optional[str] = None, emit="turn_animation_complete"):
        self.event = event
        self.emit = emit
        func_name = update["name"]
        args = update.get("args", [])

        if func_name in ANIMATIONS:
            self.init = lambda: ANIMATIONS[func_name]["init"](self, *args)
            self.update = lambda: ANIMATIONS[func_name]["update"](self)

    cls.__init__ = __init__
    return cls
