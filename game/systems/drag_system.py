import arcade

from engine.core.system import system, System


@system
class DragSystem(System):
    dragged_sprite = None
    drag_offset_x = 0
    drag_offset_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        hit_sprites = arcade.get_sprites_at_point((x, y), self.sprites)
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
        if self.dragged_sprite:
            temp_list = arcade.SpriteList()
            temp_list.append(self.dragged_sprite)
            temp_list.draw()
