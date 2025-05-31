import arcade

from engine.core.system import system, get_entity_value
from engine.utils.math import collides_with_point
from game.components import Size, Angle
from game.components.position import Position
from game.components.text import Text
from game.components.on_click import OnClick


@system
class ButtonSystem:
    def __init__(self, context):
        self.context = context

    def on_mouse_press(self, entities, x, y, button):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        for entity in entities:
            if Text in entity.components and OnClick in entity.components:
                position = entity.components[Position]
                size = entity.components[Size]
                if collides_with_point(arcade.XYWH(position.x, position.y, size.width, size.height), (x, y)):
                    entity.components[OnClick].action()
                    self.context.emit("on_mouse_click")

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
