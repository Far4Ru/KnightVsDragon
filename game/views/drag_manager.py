import arcade


class DragManager:
    def __init__(self, grid):
        self.grid = grid
        self.dragged_sprite = None
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        
        self.draggable_sprites = arcade.SpriteList()
        
        sprites_data = [
            ":resources:images/animated_characters/female_person/femalePerson_idle.png",
            ":resources:images/animated_characters/male_person/malePerson_idle.png",
            ":resources:images/tiles/grassMid.png",
            ":resources:images/tiles/boxCrate_double.png",
        ]
        
        for i, texture_path in enumerate(sprites_data):
            sprite = arcade.Sprite(texture_path, scale=0.5)
            sprite.center_x = 50 + i * 100
            sprite.center_y = 50
            self.draggable_sprites.append(sprite)

    def on_mouse_press(self, x, y, button, modifiers):
        hit_sprites = arcade.get_sprites_at_point((x, y), self.draggable_sprites)
        if hit_sprites:
            sprite = hit_sprites[-1]
            self.dragged_sprite = arcade.Sprite(
                sprite.texture.file_path,
                center_x=x,
                center_y=y,
                scale=0.5
            )
            self.drag_offset_x = x - sprite.center_x
            self.drag_offset_y = y - sprite.center_y
            return
        
        # On grid removing
        grid_sprite = self.grid.get_sprite_at_position(x, y)
        if grid_sprite and button == arcade.MOUSE_BUTTON_RIGHT:
            grid_sprite.texture = grid_sprite.original_texture

    def on_mouse_release(self, x, y, button, modifiers):
        if self.dragged_sprite and button == arcade.MOUSE_BUTTON_LEFT:
            target_sprite = self.grid.get_sprite_at_position(x, y)
            if target_sprite:
                target_sprite.texture = arcade.load_texture(self.dragged_sprite.texture.file_path)
            
            self.dragged_sprite = None

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.dragged_sprite:
            self.dragged_sprite.center_x = x - self.drag_offset_x
            self.dragged_sprite.center_y = y - self.drag_offset_y

    def draw(self):
        self.draggable_sprites.draw()
        
        if self.dragged_sprite:
            temp_list = arcade.SpriteList()
            temp_list.append(self.dragged_sprite)
            temp_list.draw()