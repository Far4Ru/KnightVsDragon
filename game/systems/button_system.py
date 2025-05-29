import arcade

from engine.core.system import system
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
                btn = entity.components[Text]
                position = entity.components[Position]
                if (position.x - btn.width / 2 <= x <= position.x + btn.width / 2 and
                        position.y - btn.height / 2 <= y <= position.y + btn.height / 2):
                    entity.components[OnClick].on_click()

    def on_mouse_motion(self, entities, x, y):
        for entity in entities:
            if Text in entity.components and OnClick in entity.components:
                btn = entity.components[Text]
                position = entity.components[Position]
                if (position.x - btn.width / 2 <= x <= position.x + btn.width / 2 and
                        position.y - btn.height / 2 <= y <= position.y + btn.height / 2):
                    btn.color = arcade.color.BLUE
                else:
                    btn.color = arcade.color.BLACK
