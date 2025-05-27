from engine.engine import GameEngine


class Component:
    def update(self, dt):
        pass

class SpriteComponent(Component):
    def __init__(self, texture_key):
        self.texture = GameEngine().resource_manager.get_texture(texture_key)

COMPONENT_CLASSES = {}

def register_component(cls):
    COMPONENT_CLASSES[cls.__name__] = cls
    return cls