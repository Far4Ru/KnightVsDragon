from functools import wraps
from typing import Dict, List
from engine.core.system import system
from engine.core.system import System
from game.components.turn import Turn


@system
class TurnSystem(System):
    current_turn: int = 0
    last_turn: int = 0

    def start(self, entities):
        self.current_turn = 0

        def next_turn():
            self.current_turn += 1
            if self.current_turn > self.last_turn:
                self.current_turn = 0
            self.event_bus.emit("turn_update", self.current_turn)
        self.event_bus.subscribe("next_turn", self, next_turn)

        for entity in entities:
            if entity.has_component(Turn):
                turn = entity.get_component(Turn)
                if turn.order > self.last_turn:
                    self.last_turn = turn.order

                def turn_wrapper(context):
                    def turn_function(event):
                        event.turn.current = context.current_turn == event.turn.order
                    return turn_function

                turn_callback = turn_wrapper(self)

                self.event_bus.subscribe("turn_update", entity, turn_callback)

    def update(self, entities):
        pass
