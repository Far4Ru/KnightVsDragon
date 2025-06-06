from engine.core.system import system
from engine.core.system import System


def wrapper_check_combo(self):
    def check_combo(event):
        self.add(event["x"], event["y"], event["type"])

    return check_combo


@system
class ComboSystem(System):
    combo_grid = {}

    def start(self, entities):
        self.combo_grid = {}
        self.event_bus.subscribe("check_combo", self, wrapper_check_combo(self))

    def add(self, x, y, symbol_type):
        if not self.combo_grid.get(symbol_type, None):
            self.combo_grid[symbol_type] = []
        for grid_symbol_type in self.combo_grid.keys():
            if [x, y] in self.combo_grid[grid_symbol_type]:
                return
        self.combo_grid[symbol_type].append([x, y])
        self.check(x, y, symbol_type)
        self.event_bus.emit("next_turn", {"next": None})

    def check(self, x, y, symbol_type):
        directions = [
            [(1, 0), (0, 1)],
            [(1, 1), (-1, -1)],
            [(-1, 1), (1, -1)],
            [(-1, 0), (0, -1)],
        ]

        neighbors = []
        for direction in directions:
            direction_neighbors = []
            for dx, dy in direction:
                for i in range(1, 3):
                    if [x + dx * i, y + dy * i] in self.combo_grid[symbol_type]:
                        direction_neighbors.append([x + dx * i, y + dy * i])
                    else:
                        break
            if len(direction_neighbors) > 1:
                neighbors.append(direction_neighbors)
        return neighbors
