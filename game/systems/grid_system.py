import copy

from engine.core.entity import Entity
from engine.core.system import system, System
from engine.utils.math import calculate_perspective_scale
from game.components import Size, Grid, Scale, Target
from game.components.animation import Animation
from game.components.condition import Condition
from game.components.droppable import Droppable
from game.components.layer import Layer
from game.components.position import Position
from game.components.sprite import Sprite
from game.components.tile import Tile


@system
class GridSystem(System):
    tiles = []

    def start(self, entities):
        for entity in entities:
            if tile := entity.get_component(Tile):
                self.tiles.append(entity)
        for entity in entities:
            if grid := entity.get_component(Grid):
                if position := entity.get_component(Position):
                    accumulated_y = 0

                    for y in range(grid.rows):
                        current_scale = calculate_perspective_scale(y, grid.rows)
                        scaled_height = grid.cell_size * current_scale
                        scaled_width = grid.cell_size * current_scale

                        total_row_width = grid.cols * scaled_width
                        start_x = (grid.cell_size * grid.cols - total_row_width) / 2

                        for x in range(grid.cols):
                            pos_x = start_x + x * scaled_width + scaled_width / 2
                            pos_y = accumulated_y + scaled_height / 2
                            tile_entity = copy.deepcopy(self.get_tile(entity, x, y))
                            self.update_tile(tile_entity, x, y, position.x + pos_x, position.y + pos_y, current_scale,
                                             scaled_width, scaled_height)
                            entities.append(tile_entity)

                        accumulated_y += scaled_height

    def update_tile(self, entity, x, y, pos_x, pos_y, current_scale, scaled_width, scaled_height):
        if tile := entity.get_component(Tile):
            tile.x = x
            tile.y = y
        if position := entity.get_component(Position):
            position.x = pos_x
            position.y = pos_y
        if scale := entity.get_component(Scale):
            scale.scale = current_scale
        if size := entity.get_component(Size):
            size.width = scaled_width
            size.height = scaled_height

    def get_tile(self, grid, x, y):
        for entity in self.tiles:
            if tile := entity.get_component(Tile):
                if target := entity.get_component(Target):
                    if target.entity == grid.type:
                        if condition := entity.get_component(Condition):
                            if condition.check(x, y):
                                return entity
