import arcade
from pyglet.math import Vec2

from engine.core.entity import Entity
from engine.core.system import system, System
from engine.utils.math import collides_with_point, calculate_perspective_scale
from game.components import Size, Angle, Grid, Scale
from game.components.droppable import Droppable
from game.components.layer import Layer
from game.components.position import Position
from game.components.on_click import OnClick
from game.components.sprite import Sprite
from game.components.tile import Tile


@system
class GridSystem(System):
    isInited = False

    def start(self, entities):
        for entity in entities:
            if entity.has_component(Grid):
                grid = entity.get_component(Grid)
                position = entity.get_component(Position)
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
                        tile_entity = Entity("none")
                        tile_entity.add_component(Tile(x, y))
                        tile_entity.add_component(Sprite(texture=grid.texture))
                        tile_entity.add_component(Position(x=position.x + pos_x, y=position.y + pos_y))
                        tile_entity.add_component(Scale(scale=current_scale))
                        tile_entity.add_component(Size(width=scaled_width, height=scaled_height))
                        tile_entity.add_component(Layer(level=1))
                        tile_entity.add_component(Droppable())
                        entities.append(tile_entity)

                    accumulated_y += scaled_height
                continue
