import arcade
from pyglet.math import Vec2

from engine.core.system import system, System
from engine.engine import GameEngine
from engine.utils.math import collides_with_point
from game.components import Size, Grid
from game.components.draggable import Draggable
from game.components.droppable import Droppable
from game.components.position import Position
from game.components.sprite import Sprite


@system
class DragSystem(System):
    isInited = False
    dragged_sprite = None
    drag_offset_x = 0
    drag_offset_y = 0

    def update(self, entities):
        if self.isInited:
            return
        self.isInited = True
        for entity in entities:
            if Sprite in entity.components:
                if Draggable in entity.components:
                    def make_on_click(context, e):
                        def on_click(event):
                            position = e.components[Position]
                            sprite = e.components[Sprite]
                            if collides_with_point(
                                    arcade.XYWH(position.x, position.y, 200, 200),
                                    (event.x, event.y)
                            ):
                                context.dragged_sprite = arcade.Sprite(
                                    GameEngine().texture_manager.get(sprite.texture),
                                    center_x=event.x,
                                    center_y=event.y,
                                    scale=1
                                )
                                context.drag_offset_x = event.x - position.x
                                context.drag_offset_y = event.y - position.y
                                return

                        return on_click

                    on_click_callback = make_on_click(self, entity)
                    self.event_bus.subscribe("on_mouse_click", entity, on_click_callback)
                if Droppable in entity.components:
                    def make_on_hover(context, e):
                        def on_hover(event):
                            # position = e.components[Position]
                            # size = e.components[Size]
                            # if Grid in entity.components:
                            #     target_sprite = self.grid.get_sprite_at_position(x, y)
                            # if target_sprite:
                            #     target_sprite.texture = arcade.load_texture(self.dragged_sprite.texture.file_path)

                            context.dragged_sprite = None

                        return on_hover

                    on_hover_callback = make_on_hover(self, entity)
                    self.event_bus.subscribe("on_mouse_drop", entity, on_hover_callback)

    def on_mouse_press(self, entities, x, y, button):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        self.event_bus.emit("on_mouse_click", Vec2(x, y))

    def on_mouse_release(self, entities, x, y, button, modifiers):
        if self.dragged_sprite and button == arcade.MOUSE_BUTTON_LEFT:
            self.event_bus.emit("on_mouse_drop", Vec2(x, y))

    def on_mouse_drag(self, entities, x, y, dx, dy, buttons, modifiers):
        if self.dragged_sprite:
            self.dragged_sprite.center_x = x - self.drag_offset_x
            self.dragged_sprite.center_y = y - self.drag_offset_y

    def draw(self):
        if self.dragged_sprite:
            temp_list = arcade.SpriteList()
            temp_list.append(self.dragged_sprite)
            temp_list.draw()
