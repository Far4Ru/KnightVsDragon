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
        self.event_bus.clear()
        self.systems = []
        for system in self.config["systems"]:
            self.systems.append(SYSTEM_CLASSES[system](self.event_bus))
        self.load()
        self.start()

    def load(self):
        self.entities = []
        for entity in self.config["entities"]:
            self.entities.append(Entity(self.config["entity_config"], entity))

    @systems_call("start")
    def start(self, system):
        system.start(self.entities)

    @systems_call("on_mouse_press")
    def on_mouse_press(self, system, x, y, button, modifiers):
        system.on_mouse_press(self.entities, x, y, button)

    @systems_call("on_mouse_motion", after="update")
    def on_mouse_motion(self, system, x: int, y: int, dx: int, dy: int):
        system.on_mouse_motion(self.entities, x, y)

    @systems_call("on_mouse_drag", after="update")
    def on_mouse_drag(self, system, x, y, dx, dy, buttons, modifiers):
        system.on_mouse_drag(self.entities, x, y, dx, dy, buttons, modifiers)

    @systems_call("on_mouse_release", after="update")
    def on_mouse_release(self, system, x, y, button, modifiers):
        system.on_mouse_release(self.entities, x, y, button, modifiers)

    @systems_call("on_update", after="update")
    def on_update(self, system, delta_time):
        system.on_update(self.entities, delta_time)

    @systems_call("update", before="update_events")
    def update(self, system):
        system.update(self.entities)

    @systems_call("draw", before="clear")
    def on_draw(self, system):
        system.draw()

    def update_events(self):
        self.event_bus.process()
