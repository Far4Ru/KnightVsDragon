import arcade
from pyglet.math import Vec2

from engine.core.system import system, System
from engine.utils.math import collides_with_point
from game.components import Size, Angle
from game.components.on_hover import OnHover
from game.components.position import Position
from game.components.text import Text
from game.components.on_click import OnClick


@system
class ButtonSystem(System):
    isInited = False

    def update(self, entities):
        if self.isInited:
            return
        self.isInited = True
        for entity in entities:
            if Text in entity.components:
                if OnClick in entity.components:
                    def make_on_click(e):
                        def on_click(event):
                            angle = entity.get_component(Angle).degree
                            position = e.components[Position]
                            size = e.components[Size]
                            if collides_with_point(
                                    arcade.XYWH(position.x, position.y, size.width, size.height),
                                    (event.x, event.y),
                                    angle
                            ):
                                e.components[OnClick].action()

                        return on_click

                    on_click_callback = make_on_click(entity)
                    self.event_bus.subscribe("on_mouse_click", entity, on_click_callback)
                if OnHover in entity.components:
                    entity.components[OnHover].target = entity.components[Text]

                    def make_on_hover(e):
                        def on_hover(event):
                            angle = entity.get_component(Angle).degree
                            position = e.components[Position]
                            size = e.components[Size]
                            if collides_with_point(
                                    arcade.XYWH(position.x, position.y, size.width, size.height),
                                    (event.x, event.y),
                                    angle
                            ):
                                e.components[OnHover].is_hovered = True
                            else:
                                e.components[OnHover].is_hovered = False
                            e.components[OnHover].action()

                        return on_hover

                    on_hover_callback = make_on_hover(entity)
                    self.event_bus.subscribe("on_mouse_hover", entity, on_hover_callback)

    def on_mouse_press(self, entities, x, y, button):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        self.event_bus.emit("on_mouse_click", Vec2(x, y))

    def on_mouse_motion(self, entities, x, y):
        self.event_bus.emit("on_mouse_hover", Vec2(x, y))
