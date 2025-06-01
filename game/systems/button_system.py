import arcade
from pyglet.math import Vec2

from engine.core.system import system, get_entity_value, System
from engine.utils.math import collides_with_point
from game.components import Size, Angle
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
            if Text in entity.components and OnClick in entity.components:
                def make_check_cords(e):
                    def check_cords(event):
                        position = e.components[Position]
                        size = e.components[Size]
                        if collides_with_point(
                                arcade.XYWH(position.x, position.y, size.width, size.height),
                                (event.x, event.y)
                        ):
                            print(position)
                            e.components[OnClick].action()

                    return check_cords

                callback = make_check_cords(entity)
                self.event_bus.subscribe("on_mouse_click", entity, callback)

    def on_mouse_press(self, entities, x, y, button):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        self.event_bus.emit("on_mouse_click", Vec2(x, y))

    def on_mouse_motion(self, entities, x, y):
        for entity in entities:
            angle = get_entity_value(entity, Angle).degree
            position = get_entity_value(entity, Position)
            if Text in entity.components and OnClick in entity.components:
                text = entity.components[Text]
                size = entity.components[Size]
                if collides_with_point(arcade.XYWH(position.x, position.y, size.width, size.height), (x, y), angle):
                    text.color = arcade.color.BLUE
                else:
                    text.color = arcade.color.BLACK
