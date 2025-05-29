from engine.core.scene import Scene
from game.components.size import Size
from game.components.angle import Angle
from game.systems.button_system import ButtonSystem
from game.systems.rendering_system import RenderingSystem
from game.systems.sound_system import SoundSystem


class TestView(Scene):
    def setup(self, systems=None):
        super().setup(["SoundSystem", "ButtonSystem", "RenderingSystem"])

    def load(self, entities=None):
        super().load(["knight", "dragon", "logo", "background", "exit_button"])
