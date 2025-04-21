from engine.managers.entity_manager import EntityPrototype

class HeroPrototype(EntityPrototype):
    def __init__(self):
        super().__init__()
        self.add_component(SpriteComponent("hero"))
        self.add_component(HealthComponent(100))
        self.add_component(MovementComponent(speed=200))