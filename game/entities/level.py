class LevelModel:
    def setup_level(self, level_id):
        engine = GameEngine()
        data = engine.resource_manager.load_level(level_id)
        
        entity_mgr = engine.entity_manager
        for tile_data in data['tiles']:
            entity_id = entity_mgr.create_entity([
                SpriteComponent(tile_data['texture']),
                TileComponent(tile_data['type']),
                PositionComponent(tile_data['x'], tile_data['y'])
            ])