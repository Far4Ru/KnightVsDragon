import arcade.color

from engine.core.scene import Scene
from game.entities.entity import Entity
from game.systems.button_system import ButtonSystem
from game.systems.rendering_system import RenderingSystem


class TestView(Scene):
    def setup(self, systems=None):
        super().setup([ButtonSystem, RenderingSystem])

    def load(self):
        self.entities.append(Entity("player"))
        self.entities.append(Entity("enemy"))
        self.entities.append(Entity("logo"))
        self.entities.append(Entity("background"))
        self.entities.append(Entity("exit_button"))
