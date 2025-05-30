import arcade
from dataclasses import dataclass

from engine.core.component import component
from engine.engine import GameEngine


@component
@dataclass
class Grid:
    cols: int
    rows: int


class GridOld:
    def __init__(self, rows, cols):
        self.x = 125
        self.y = 180
        self.rows = rows
        self.cols = cols
        self.sprite_list = arcade.SpriteList()
        self.cell_size = 128
        self.gap_x = 0
        self.gap_y = 0
        self.base_scale = 0.8
        self.scale_reduction = 0.2
        self.perspective_factor = 0.7
        self.setup_grid()
    
    def calculate_perspective_scale(self, y, rows):
        
        normalized_y = y / (rows - 1) if rows > 1 else 0
        
        scale = self.base_scale - (self.base_scale - self.scale_reduction) * (normalized_y ** self.perspective_factor)
        
        return scale
    
    def setup_grid(self):
        accumulated_y = 0
        for y in range(self.rows):
            current_scale = self.calculate_perspective_scale(y, self.rows)
            scaled_height = self.cell_size * current_scale
            scaled_width = self.cell_size * current_scale
            
            total_row_width = self.cols * scaled_width
            start_x = (self.cell_size * self.cols - total_row_width) / 2
            
            for x in range(self.cols):
                pos_x = start_x + x * scaled_width + scaled_width / 2
                pos_y = accumulated_y + scaled_height / 2
                
                sprite = arcade.Sprite(
                    GameEngine().texture_manager.get("cell"),
                    center_x=self.x + pos_x,
                    center_y=self.y + pos_y,
                    scale=current_scale,
                )
                sprite.original_texture = sprite.texture
                self.sprite_list.append(sprite)

            accumulated_y += scaled_height

    def get_sprite_at_position(self, x, y):
        hit_sprites = arcade.get_sprites_at_point((x, y), self.sprite_list)
        return hit_sprites[0] if hit_sprites else None

    def draw(self):
        self.sprite_list.draw()
