class EntityInspector:
    def draw_overlay(self):
        for entity in self.entity_manager.entities:
            pos = entity.get(Position)
            imgui.text(f"Entity {entity.id} at ({pos.x}, {pos.y})")