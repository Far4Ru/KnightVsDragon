import arcade

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cell_size = 128
        self.sprite_list = arcade.SpriteList()
        self.setup_grid()

    def setup_grid(self):
        for y in range(self.rows):
            for x in range(self.cols):
                sprite = arcade.Sprite(
                    ":resources:images/tiles/boxCrate_double.png",
                    center_x=64 + x * self.cell_size,
                    center_y=64 + y * self.cell_size * (1/(y/9+1)),
                    scale=1/(y/3+1) ,
                )
                sprite.original_texture = sprite.texture
                self.sprite_list.append(sprite)

    def get_sprite_at_position(self, x, y):
        hit_sprites = arcade.get_sprites_at_point((x, y), self.sprite_list)
        return hit_sprites[0] if hit_sprites else None

    def draw(self):
        self.sprite_list.draw()