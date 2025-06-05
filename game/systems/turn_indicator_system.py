from engine.core.system import system
from engine.core.system import System
from game.components.turn_indicator import TurnIndicator


@system
class TurnIndicatorSystem(System):
    animations = []

    def start(self, entities):
        for entity in entities:
            if entity.has_component(TurnIndicator):
                pass

    def update(self, entities):
        for entity in entities:
            if turn_indicator := entity.get_component(TurnIndicator):
                    pass

