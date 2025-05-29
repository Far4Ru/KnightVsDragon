from engine.core.component import COMPONENT_CLASSES


class Entity:
    def __init__(self, config_name, entity_type=None):
        self.config_name = config_name
        self.components = {}
        self.type = entity_type
        if entity_type:
            self.load()

    def add_component(self, component):
        self.components[type(component)] = component

    def load(self):
        from engine.engine import GameEngine
        templates = GameEngine().config_manager.get(self.config_name)
        for comp_name, comp_data in templates[self.type]["components"].items():
            print(COMPONENT_CLASSES)
            print(comp_name)
            component_class = COMPONENT_CLASSES[comp_name]
            self.add_component(component_class(**comp_data))
        return self
