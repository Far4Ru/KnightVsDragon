import arcade

from game.components.sprite import Position
from game.components.text_button import Action, TextButton, Clickable


class ButtonSystem:
    def __init__(self, context):
        self.context = context

    def on_mouse_press(self, entities, x, y, button):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        for entity in entities:
            if TextButton in entity.components and Clickable in entity.components:
                btn = entity.components[TextButton]
                position = entity.components[Position]
                if (position.x - btn.width / 2 <= x <= position.x + btn.width / 2 and
                        position.y - btn.height / 2 <= y <= position.y + btn.height / 2):
                    entity.components[Clickable].on_click()
                    if Action in entity.components:
                        self.switch_view(entity.components[Action].target_view)

    def on_mouse_motion(self, entities, x, y):
        for entity in entities:
            if TextButton in entity.components and Clickable in entity.components:
                btn = entity.components[TextButton]
                position = entity.components[Position]
                if (position.x - btn.width / 2 <= x <= position.x + btn.width / 2 and
                        position.y - btn.height / 2 <= y <= position.y + btn.height / 2):
                    btn.color = arcade.color.BLUE
                else:
                    btn.color = arcade.color.BLACK


    def switch_view(self, view_name: str):
        if view_name == "game":
            self.window.show_view(self.window.game_view)
        elif view_name == "menu":
            self.window.show_view(self.window.menu_view)
