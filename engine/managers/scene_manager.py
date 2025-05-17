import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
SCREEN_TITLE = "Богатырь против Змея Горыныча"


class SceneManager(arcade.Window):
    def get_clipboard_text(self) -> str:
        pass

    def set_clipboard_text(self, text: str) -> None:
        pass

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.current_scene = None
    
    def change_scene(self, new_scene):
        if self.current_scene:
            pass
        self.current_scene = new_scene
        new_scene.setup()
    
    def on_draw(self):
        if self.current_scene:
            self.current_scene.on_draw()
    
    def on_update(self, delta_time):
        if self.current_scene:
            self.current_scene.on_update(delta_time)
    
    def on_key_press(self, key, modifiers):
        if self.current_scene:
            self.current_scene.on_key_press(key, modifiers)
