import arcade
from engine.core.scene import Scene
from engine.engine import GameEngine
from game.components.component import Clickable, TextButton
from game.entities.entity import Entity
from game.systems.button_system import ButtonSystem
from game.systems.rendering_system import RenderingSystem

def apply_entity(method, before=None, after=None):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if (before and hasattr(self, before)):
                getattr(self, before)()
            for system in self.systems:
                if hasattr(system, method):
                    func(self, system, *args, **kwargs)
            if (after and hasattr(self, after)):
                getattr(self, after)()
        return wrapper
    return decorator

class TestView(Scene):
    def __init__(self):
        super().__init__()
        self.entities = []
        self.systems = [
            # PlayerControlSystem(),
            # EnemyAISystem(),
            # MovementSystem(),
            ButtonSystem(self),
            RenderingSystem(self),
        ]
    
    def setup(self):
        self.load()
        self.update()

    def load(self):
        self.entities.append(Entity("player"))
        self.entities.append(Entity("enemy"))
        self.entities.append(Entity("logo"))
        self.entities.append(Entity("background"))
        quit_btn = Entity()
        quit_btn.add_component(TextButton("Выход", 600, 150))
        quit_btn.add_component(Clickable(lambda: arcade.exit()))
        self.entities.append(quit_btn)

    @apply_entity("on_mouse_press")
    def on_mouse_press(self, system, x, y, button, modifiers):
        system.on_mouse_press(self.entities, x, y, button)

    @apply_entity("on_mouse_motion", after="update")
    def on_mouse_motion(self, system, x: int, y: int, dx: int, dy: int):
        system.on_mouse_motion(self.entities, x, y)

    @apply_entity("update")
    def update(self, system):
        system.update(self.entities)

    @apply_entity("on_mouse_motion", before="clear")
    def on_draw(self, system):
        system.draw()