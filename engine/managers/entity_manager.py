class EntityManager:
    def __init__(self):
        self._entities = {}
        
    def create_entity(self, components: list) -> int:
        entity_id = generate_id()
        self._entities[entity_id] = components
        return entity_id
        
    def get_component(self, entity_id, component_type):
        for comp in self._entities.get(entity_id, []):
            if isinstance(comp, component_type):
                return comp