import arcade
from pyglet.math import Vec2

from engine.core.system import system, System
from engine.utils.math import collides_with_point
from game.components import Size, Angle
from game.components.on_hover import OnHover
from game.components.position import Position
from game.components.text import Text
from game.components.on_click import OnClick


def make_on_hover(on_hover_component, entity):
    def on_hover(event):
        if text := entity.get_component(Text):
            on_hover_component.target = text
            angle_degree = 0
            if angle := entity.get_component(Angle):
                angle_degree = angle.degree
            if (position := entity.get_component(Position)) and (size := entity.get_component(Size)):
                if collides_with_point(
                        arcade.XYWH(position.x, position.y, size.width, size.height),
                        (event.x, event.y),
                        angle_degree
                ):
                    on_hover_component.is_hovered = True
                else:
                    on_hover_component.is_hovered = False
                on_hover_component.action()

    return on_hover


def make_on_click(on_click_component, entity):
    def on_click(event):
        angle_degree = 0
        if angle := entity.get_component(Angle):
            angle_degree = angle.degree
        if (position := entity.get_component(Position)) and (size := entity.get_component(Size)):
            if collides_with_point(
                    arcade.XYWH(position.x, position.y, size.width, size.height),
                    (event.x, event.y),
                    angle_degree
            ):
                on_click_component.action()

    return on_click


@system
class ButtonSystem(System):
    def start(self, entities):
        for entity in entities:
            if on_click_component := entity.get_component(OnClick):
                self.event_bus.subscribe("on_mouse_click", entity, make_on_click(on_click_component, entity))
            if on_hover_component := entity.get_component(OnHover):
                self.event_bus.subscribe("on_mouse_hover", entity, make_on_hover(on_hover_component, entity))

    def on_mouse_press(self, entities, x, y, button):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        self.event_bus.emit("on_mouse_click", Vec2(x, y))

    def on_mouse_motion(self, entities, x, y):
        self.event_bus.emit("on_mouse_hover", Vec2(x, y))
