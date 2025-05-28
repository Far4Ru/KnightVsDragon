from engine.core.component import COMPONENT_CLASSES
from engine.engine import GameEngine

class Entity:
    def __init__(self, type = None):
        self.components = {}
        self.type = type
        if (type):
            self.load()

    def add_component(self, component):
        self.components[type(component)] = component

    def load(self):
        templates = GameEngine().config_manager.get("entity_config")
        for comp_name, comp_data in templates[self.type]["components"].items():
            component_class = COMPONENT_CLASSES[comp_name]
            self.add_component(component_class(**comp_data))
        return self