from engine.core.scene import Scene

class GameView(Scene):
    def __init__(self, level_id):
        self.level_id = level_id
        
    def setup(self):
        engine = GameEngine()
        level_data = engine.resource_manager.load_level(self.level_id)
        self.level_model = LevelModel(level_data)
        
    def on_draw(self):
        self.level_model.draw()