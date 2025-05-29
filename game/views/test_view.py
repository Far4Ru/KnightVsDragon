from engine.core.scene import Scene
from game.systems import *


class TestView(Scene):
    def setup(self, systems=None):
        super().setup(["SoundSystem", "ButtonSystem", "RenderingSystem"])

    def load(self, entities=None):
        super().load(["knight", "dragon", "logo", "background", "exit_button"])
