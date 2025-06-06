from engine.core.system import system
from engine.core.system import System
from game.components import Target
from game.components.damage import Damage


def wrapper_update_damage(self, entity):
    def update_damage(event):
        if damage := entity.get_component(Damage):
            if target := entity.get_component(Target):
                if target.entity == event["target_entity"]:
                    damage.value = event["damage"]
    return update_damage


@system
class DamageSystem(System):
    combo_grid = {}

    def start(self, entities):
        self.combo_grid = {}
        for entity in entities:
            if damage := entity.get_component(Damage):
                self.event_bus.subscribe("update_damage", entity, wrapper_update_damage(self, entity))
