from engine.core.system import system
from engine.core.system import System
from game.components.sprite import Sprite
from game.components.upgradable import Upgradable


def wrapper_upgrade(self, entity):
    def upgrade(event):
        try:
            if upgradable := entity.get_component(Upgradable):
                value = event["value"]
                if value == 0:
                    if sprite := entity.get_component(Sprite):
                        sprite.texture = event["texture"]
                        return
                index = upgradable.texture_names.index(event["texture"])
                if len(upgradable.texture_names) > (index + value):
                    index += value
                else:
                    index = len(upgradable.texture_names) - 1
                symbol_type = upgradable.texture_names[index]
                x, y = event["x"], event["y"]
                self.event_bus.emit("check_combo", {"x": x, "y": y, "type": symbol_type})
                self.event_bus.emit("update_damage", {"target_entity": "dragon", "damage": (index + 1) * 10})
                self.event_bus.emit("update_tile", {"x": x, "y": y, "texture": symbol_type})
                if sprite := entity.get_component(Sprite):
                    sprite.texture = symbol_type
        except ValueError:
            pass

    return upgrade


@system
class UpgradeSystem(System):
    combo_grid = {}

    def start(self, entities):
        self.combo_grid = {}
        for entity in entities:
            if upgradable := entity.get_component(Upgradable):
                self.event_bus.subscribe("upgrade", entity, wrapper_upgrade(self, entity))
