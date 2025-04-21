class GameController:
    def on_mouse_press(self, x, y):
        engine = GameEngine()
        for entity_id in engine.entity_manager.get_entities_with(PositionComponent):
            pos = engine.entity_manager.get_component(entity_id, PositionComponent)
            if pos.collides(x, y):
                tile = engine.entity_manager.get_component(entity_id, TileComponent)
                tile.is_selected = True
                self._check_matches()