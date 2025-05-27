from engine.core.component import COMPONENT_CLASSES
from engine.engine import GameEngine

class Entity:
    def __init__(self):
        self.components = {}

    def add_component(self, component):
        self.components[type(component)] = component

    def load(self, type):
        templates = GameEngine().config_manager.get("entity_config")
        for comp_name, comp_data in templates[type]["components"].items():
            component_class = COMPONENT_CLASSES[comp_name]
            self.add_component(component_class(**comp_data))
        return self