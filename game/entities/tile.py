from engine.core.component import Component

class TileComponent(Component):
    def __init__(self, tile_type):
        self.type = tile_type
        self.is_selected = False
