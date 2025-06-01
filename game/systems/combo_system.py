class MatchingSystem(System):
    def __init__(self, event_bus):
        event_bus.subscribe(TileSelectedEvent, self.on_tile_selected)
        
    def on_tile_selected(self, event):
        if self.check_match(event.x, event.y):
            self.event_bus.post(MatchFoundEvent(...))
            self.entity_manager.destroy_entities(matched_entities)