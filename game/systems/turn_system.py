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
        
        for entity in entities:
            if entity.has_component(Turn):
                turn = entity.get_component(Turn)
                if turn.order > self.last_turn:
                    self.last_turn = turn.order
                def turn_wrapper(context):
                    def turn_function(event):
                        if context.current_turn == event.turn.order:
                            context.current_turn = event.turn.order + 1
                            if context.current_turn > context.last_turn:
                                context.current_turn = 0
                            event.turn.current = False
                    return turn_function

                turn_callback = turn_wrapper(self)

                self.event_bus.subscribe("next_turn", entity, turn_callback)

    def update(self, entities):
        pass
