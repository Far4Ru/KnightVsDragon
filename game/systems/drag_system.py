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
from game.components.tile import Tile


def make_on_drag(self, draggable, entity):
    def on_drag(event):
        if draggable.active:
            if (position := entity.get_component(Position)) and\
                    (size := entity.get_component(Size)) and\
                    (sprite := entity.get_component(Sprite)):
                if collides_with_point(
                        arcade.XYWH(position.x, position.y, size.width, size.height),
                        (event.x, event.y)
                ):
                    self.target = entity
                    self.dragged_sprite_name = sprite.texture
                    self.dragged_sprite = arcade.Sprite(
                        GameEngine().texture_manager.get(sprite.texture),
                        center_x=event.x,
                        center_y=event.y,
                        scale=1
                    )
                    self.drag_offset_x = event.x - position.x
                    self.drag_offset_y = event.y - position.y

    return on_drag


def make_on_drop(self, droppable, entity, entities):
    def on_drop(event):
        if not droppable.droppable:
            self.dragged_sprite = None
            self.dragged_sprite_name = None
            return
        if (position := entity.get_component(Position)) and\
                (size := entity.get_component(Size)) and\
                (sprite := entity.get_component(Sprite)):
            if collides_with_point(
                    arcade.XYWH(position.x, position.y, size.width, size.height),
                    (event.x, event.y)
            ):
                if tile := entity.get_component(Tile):

                    self.event_bus.emit("check_combo", {"x": tile.x, "y": tile.y, "type": self.target.get_component(Sprite).texture})
                self.dragged_sprite = None
                self.dragged_sprite_name = None

    return on_drop


@system
class DragSystem(System):
    dragged_sprite = None
    dragged_sprite_name = None
    drag_offset_x = 0
    drag_offset_y = 0

    def start(self, entities):
        for entity in entities:
            if draggable := entity.get_component(Draggable):
                self.event_bus.subscribe("on_drag_start", entity, make_on_drag(self, draggable, entity))
            if droppable := entity.get_component(Droppable):
                self.event_bus.subscribe("on_mouse_drop", entity, make_on_drop(self, droppable, entity, entities))

    def on_mouse_press(self, entities, x, y, button):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        self.event_bus.emit("on_drag_start", Vec2(x, y))

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
