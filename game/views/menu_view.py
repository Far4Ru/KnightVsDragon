from engine.managers.scene_manager import Scene

class MenuView(Scene):
    def setup(self):
        engine = GameEngine()
        
        # Загрузка через ResourceManager
        bg_texture = engine.resource_manager.get_texture("menu_bg")
        self.bg_sprite = arcade.Sprite(texture=bg_texture)
        
        # Создание кнопок через UI менеджер
        engine.ui_manager.add_button(
            "start_btn", 
            x=100, y=200,
            texture="btn_start",
            callback=self._on_start
        )

    def _on_start(self):
        engine = GameEngine()
        engine.scene_manager.switch_to(CharacterSelectView())