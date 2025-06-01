from typing import Type, Optional

from engine.core.component import COMPONENT_CLASSES, Component


class Entity:
    def __init__(self, config_name, entity_type=None):
        self.config_name = config_name
        self.components = {}
        self.type = entity_type
        if entity_type:
            self.load()

    def add_component(self, component):
        self.components[type(component)] = component

    def get_component(self, component_type: Type[Component]) -> Optional[Component]:
        if self.has_component(component_type):
            return self.components.get(component_type)
        return component_type()

    def has_component(self, component_type: Type[Component]) -> bool:
        return component_type in self.components

    def load(self):
        from engine.engine import GameEngine
        templates = GameEngine().config_manager.get(self.config_name)
        for comp_name, comp_data in templates[self.type]["components"].items():
            component_class = COMPONENT_CLASSES[comp_name]
            self.add_component(component_class(**comp_data))
        return self
