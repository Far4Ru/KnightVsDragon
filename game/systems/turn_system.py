from engine.core.system import system
from engine.core.system import System
from game.components.animation import Animation
from game.components.turn import Turn


def next_turn_wrapper(self):
    def next_turn(event):
        self.current_turn = event["next"] or (self.current_turn + 1)
        if self.current_turn > self.last_turn:
            self.current_turn = 0
        self.event_bus.emit("turn_update", {"current": self.current_turn})

    return next_turn


@system
class TurnSystem(System):
    current_turn: int = 0
    last_turn: int = 0

    def start(self, entities):
        self.current_turn = 0

        self.event_bus.subscribe("next_turn", self, next_turn_wrapper(self))

        for entity in entities:
            if turn := entity.get_component(Turn):
                if turn.order > self.last_turn:
                    self.last_turn = turn.order
                turn.current = self.current_turn == turn.order

                def turn_wrapper(context, turn_value):
                    def turn_function(event):
                        turn_value.current = context.current_turn == turn_value.order
                    return turn_function

                self.event_bus.subscribe("turn_update", entity, turn_wrapper(self, turn))

    def update(self, entities):
        for entity in entities:
            if turn := entity.get_component(Turn):
                if animation := entity.get_component(Animation):
                    animation.active = turn.current
