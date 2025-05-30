import arcade
from pyglet.math import Vec2

from engine.core.system import system
from game.components import Size
from game.components.position import Position
from game.components.text import Text
from game.components.on_click import OnClick


def collides_with_point(rect: arcade.XYWH, point: tuple[float | int, float | int] | Vec2):
    position = Vec2(*point) if not isinstance(point, Vec2) else point
    return (rect.x - rect.width / 2 <= position.x <= rect.x + rect.width / 2 and
            rect.y - rect.height / 2 <= position.y <= rect.y + rect.height / 2)


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

    def on_mouse_motion(self, entities, x, y):
        for entity in entities:
            if Text in entity.components and OnClick in entity.components:
                text = entity.components[Text]
                position = entity.components[Position]
                size = entity.components[Size]
                if collides_with_point(arcade.XYWH(position.x, position.y, size.width, size.height), (x, y)):
                    text.color = arcade.color.BLUE
                else:
                    text.color = arcade.color.BLACK
