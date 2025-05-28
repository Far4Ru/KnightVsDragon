import arcade

from game.components.component import Action, Clickable, TextButton


class ButtonSystem:
    def __init__(self, context):
        self.context = context

    def on_mouse_press(self, entities, x, y, button):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        for entity in entities:
            if TextButton in entity.components and Clickable in entity.components:
                btn = entity.components[TextButton]
                if (btn.x - btn.width/2 <= x <= btn.x + btn.width/2 and
                    btn.y - btn.height/2 <= y <= btn.y + btn.height/2):
                    entity.components[Clickable].on_click()
                    if Action in entity.components:
                        self.switch_view(entity.components[Action].target_view)

    def on_mouse_motion(self, entities, x, y):
        for entity in entities:
            if TextButton in entity.components and Clickable in entity.components:
                btn = entity.components[TextButton]
                if (btn.x - btn.width/2 <= x <= btn.x + btn.width/2 and
                    btn.y - btn.height/2 <= y <= btn.y + btn.height/2):
                    btn.color = arcade.color.BLUE

    def switch_view(self, view_name: str):
        if view_name == "game":
            self.window.show_view(self.window.game_view)
        elif view_name == "menu":
            self.window.show_view(self.window.menu_view)