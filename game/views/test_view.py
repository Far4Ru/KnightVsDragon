from engine.core.scene import Scene
from engine.engine import GameEngine
from game.entities.entity import Entity
from game.systems.rendering_system import RenderingSystem


class TestView(Scene):
    def __init__(self):
        super().__init__()
        self.entities = []
        self.systems = [
            # PlayerControlSystem(),
            # EnemyAISystem(),
            # MovementSystem(),
            RenderingSystem(self),
        ]
        self.setup()

    def setup(self):
        self.entities.append(Entity().load("player"))
        self.entities.append(Entity().load("enemy"))
        for system in self.systems:
            if hasattr(system, "update"):
                system.update(self.entities)

    def on_draw(self):
        self.clear()
        for system in self.systems:
            if hasattr(system, "draw"):
                system.draw()