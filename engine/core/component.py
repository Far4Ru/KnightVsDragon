class Component:
    def update(self, dt):
        pass

class SpriteComponent(Component):
    def __init__(self, texture_key):
        self.texture = GameEngine().resource_manager.get_texture(texture_key)