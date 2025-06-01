import arcade
from pyglet.math import Vec2

from engine.core.system import system, System
from engine.engine import GameEngine
from engine.utils.math import collides_with_point
from game.components import Size
from game.components.draggable import Draggable
from game.components.droppable import Droppable
from game.components.position import Position
from game.components.sprite import Sprite


@system
class DragSystem(System):
    dragged_sprite = None
    dragged_sprite_name = None
    drag_offset_x = 0
    drag_offset_y = 0

    def start(self, entities):
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
                                context.dragged_sprite_name = sprite.texture
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
                    def make_drop(context, e):
                        def drop(event):
                            if Droppable in e.components:
                                droppable = e.get_component(Droppable)
                                if not droppable.droppable:
                                    context.dragged_sprite = None
                                    context.dragged_sprite_name = None
                                    return
                                sprite = e.get_component(Sprite)
                                position = e.components[Position]
                                size = e.components[Size]
                                if collides_with_point(
                                        arcade.XYWH(position.x, position.y, size.width, size.height),
                                        (event.x, event.y)
                                ):
                                    sprite.texture = context.dragged_sprite_name
                                    context.dragged_sprite = None
                                    context.dragged_sprite_name = None

                        return drop

                    drop_callback = make_drop(self, entity)
                    self.event_bus.subscribe("on_mouse_drop", entity, drop_callback)

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
