from functools import wraps
import arcade

from engine.core.entity import Entity
from engine.core.system import SYSTEM_CLASSES
from engine.utils.event_bus import EventBus


def systems_call(method, before=None, after=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if before and hasattr(self, before):
                getattr(self, before)()
            for system in self.systems:
                if hasattr(system, method):
                    func(self, system, *args, **kwargs)
            if after and hasattr(self, after):
                getattr(self, after)()

        return wrapper

    return decorator


class Scene(arcade.View):
    event_bus = EventBus()
    systems = []
    entities = []

    def __init__(self, config):
        super(Scene, self).__init__()
        self.config = config

    def setup(self):
        print(self.systems)
        for system in self.config["systems"]:
            print(system)
            self.systems.append(SYSTEM_CLASSES[system](self.event_bus))
        self.load()
        self.update()

    def load(self):
        for entity in self.config["entities"]:
            self.entities.append(Entity(self.config["entity_config"], entity))

    @systems_call("on_mouse_press")
    def on_mouse_press(self, system, x, y, button, modifiers):
        system.on_mouse_press(self.entities, x, y, button)

    @systems_call("on_mouse_motion", after="update")
    def on_mouse_motion(self, system, x: int, y: int, dx: int, dy: int):
        system.on_mouse_motion(self.entities, x, y)

    @systems_call("update")
    def update(self, system):
        system.update(self.entities)

    @systems_call("draw", before="clear")
    def on_draw(self, system):
        system.draw()
