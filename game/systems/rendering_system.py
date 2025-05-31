import arcade
from pyglet.graphics import Batch

from config import FONT_DEFAULT
from engine.core.system import system, get_entity_value
from engine.engine import GameEngine
from engine.utils.math import calculate_perspective_scale
from game.components import Scale, Angle, Grid
from game.components.layer import Layer
from game.components.position import Position
from game.components.sprite import Sprite
from game.components.text import Text


@system
class RenderingSystem:
    def __init__(self, context):
        self.context = context
        self.layers = {}
        self.batch = Batch()
        self.elements = []
        self.need_to_update = False
        self.entities_to_update = []

    def update(self, entities):
        self.need_to_update = True
        self.entities_to_update = entities

    def _update(self):
        self.layers.clear()
        self.elements.clear()
        for entity in self.entities_to_update:
            layer_level = get_entity_value(entity, Layer).level
            scale = get_entity_value(entity, Scale).scale
            position = get_entity_value(entity, Position)
            angle = get_entity_value(entity, Angle).degree

            if Grid in entity.components:
                if layer_level not in self.layers:
                    self.layers[layer_level] = arcade.SpriteList()
                spriteLayer = self.layers[layer_level]
                grid = entity.components[Grid]
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

                        sprite = arcade.Sprite(
                            GameEngine().texture_manager.get(entity.components[Sprite].texture),
                            center_x=position.x + pos_x,
                            center_y=position.y + pos_y,
                            scale=current_scale,
                        )
                        sprite.original_texture = sprite.texture
                        spriteLayer.append(sprite)

                    accumulated_y += scaled_height
                continue
            if Sprite in entity.components:
                if layer_level not in self.layers:
                    self.layers[layer_level] = arcade.SpriteList()
                spriteLayer = self.layers[layer_level]
                if not isinstance(spriteLayer, arcade.SpriteList):
                    print(f"Ошибка использования слоя для спрайта {entity.components[Sprite]}: "
                          f"{layer_level}")
                    continue

                sprite = arcade.Sprite(
                    GameEngine().texture_manager.get(entity.components[Sprite].texture),
                    center_x=position.x,
                    center_y=position.y,
                    scale=scale,
                )
                spriteLayer.append(sprite)
                continue
            if Text in entity.components:
                if layer_level not in self.layers:
                    self.layers[layer_level] = Batch()
                batchLayer = self.layers[layer_level]
                if not isinstance(batchLayer, Batch):
                    print(f"Ошибка использования слоя для текста {entity.components[Text]}: "
                          f"{layer_level}")
                    continue
                text_button_config = entity.components[Text]
                text = GameEngine().add.text(
                    text_button_config.text, position,
                    text_button_config.color, text_button_config.font_size,
                    angle, FONT_DEFAULT, batchLayer
                )
                def print_text():
                    print("pressed")
                self.context.subscribe("on_mouse_click", text, print_text)
                self.elements.append(text)
                continue
        self.need_to_update = False

    def draw(self):
        if self.need_to_update:
            self._update()
        for layer in sorted(self.layers.keys()):
            self.layers[layer].draw()
        self.batch.draw()
