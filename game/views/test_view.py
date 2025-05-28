import arcade
from engine.core.scene import Scene
from engine.engine import GameEngine
from game.components.component import Clickable, TextButton
from game.entities.entity import Entity
from game.systems.button_system import ButtonSystem
from game.systems.rendering_system import RenderingSystem

class TestView(Scene):
    def setup(self):
        super().setup([ButtonSystem, RenderingSystem])

    def load(self):
        self.entities.append(Entity("player"))
        self.entities.append(Entity("enemy"))
        self.entities.append(Entity("logo"))
        self.entities.append(Entity("background"))
        config = {
            "exit_button": {
                "components": {
                    "Position": {"x": 600, "y": 150},
                    "Text": {"text": "Выход"},
                    "Layer": {"level": 1},
                    "Clickable": {"action": { "name": "exit", "args": []}},
                }
            },
        }
        quit_btn = Entity()
        quit_btn.add_component(TextButton("Выход", 600, 150))
        func_name = config["exit_button"]["components"]["Clickable"]["action"]["name"]
        args = config["exit_button"]["components"]["Clickable"]["action"].get("args", [])
        def exit():
            arcade.exit()
        BUTTON_ACTIONS = {
            "exit": exit
        }
        if func_name in BUTTON_ACTIONS:
            quit_btn.add_component(Clickable(lambda: BUTTON_ACTIONS[func_name](*args)))
        self.entities.append(quit_btn)
