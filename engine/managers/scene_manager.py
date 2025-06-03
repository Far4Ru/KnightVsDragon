import arcade

from engine.core.scene import Scene


class SceneManager(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.current_scene = None
    
    def change_scene(self, new_scene: Scene):
        if self.current_scene:
            pass
        self.current_scene = new_scene
        self.current_scene.setup()
        self.show_view(self.current_scene)

