import arcade
from arcade import shape_list
from pyglet.graphics import Batch

from config import FONT_DEFAULT
from engine.core.system import system, System
from engine.engine import GameEngine
from game.components import Scale, Angle, Size
from game.components.health import Health
from game.components.layer import Layer
from game.components.position import Position
from game.components.sprite import Sprite
from game.components.text import Text


@system
class RenderingSystem(System):
    layers = {}
    elements = []
    need_to_update = False
    entities_to_update = []

    def start(self, entities):
        self.update(entities)

    def update(self, entities):
        self.need_to_update = True
        self.entities_to_update = entities

    def _update(self):
        self.layers.clear()
        self.elements.clear()
        for entity in self.entities_to_update:
            layer_level = entity.get_component(Layer).level
            scale = entity.get_component(Scale).scale
            position = entity.get_component(Position)
            if entity.has_component(Health):
                health = entity.get_component(Health)
                size = entity.get_component(Size)
                rectLayer = self.get_layer(layer_level, shape_list.ShapeElementList)
                batchLayer = self.get_layer(layer_level + 1, Batch)
                if batchLayer is None:
                    continue
                if rectLayer is None:
                    continue
                text_config = entity.components[Text]
                background_rect = shape_list.create_rectangle_filled(position.x, position.y,
                                                                     size.width, size.height,
                                                                     health.background)
                rectLayer.append(background_rect)
                reduce_fill_width = ((health.max_hp - health.current_hp) / health.max_hp) * size.width
                text_config.text = f"{health.current_hp}/{health.max_hp}"
                fill_rect = shape_list.create_rectangle_filled(position.x - reduce_fill_width * 0.5, position.y,
                                                               size.width - reduce_fill_width, size.height,
                                                               health.fill)
                rectLayer.append(fill_rect)
                background_rect = shape_list.create_rectangle_outline(position.x, position.y,
                                                                      size.width, size.height,
                                                                      health.border)
                rectLayer.append(background_rect)
                text = GameEngine().add.text(
                    text_config.text, position,
                    text_config.color, text_config.font_size,
                    0, FONT_DEFAULT, batchLayer
                )
                self.elements.append(text)
                continue
            if Sprite in entity.components:
                spriteLayer = self.get_layer(layer_level)
                angle = entity.get_component(Angle).degree
                if spriteLayer is None:
                    continue
                GameEngine().add.sprite(entity.components[Sprite].texture, position, scale, spriteLayer, angle=angle)
                continue
            if Text in entity.components:
                angle = entity.get_component(Angle).degree
                batchLayer = self.get_layer(layer_level, Batch)
                if batchLayer is None:
                    continue
                text_config = entity.components[Text]
                text = GameEngine().add.text(
                    text_config.text, position,
                    text_config.color, text_config.font_size,
                    angle, FONT_DEFAULT, batchLayer
                )
                self.elements.append(text)
                continue
        self.need_to_update = False

    def get_layer(self, layer_level, layer_type=arcade.SpriteList):
        if layer_level not in self.layers:
            self.layers[layer_level] = layer_type()
        layer = self.layers[layer_level]
        if not isinstance(layer, layer_type):
            print(f"Ошибка использования слоя {layer_type}: "
                  f"{layer_level}")
            return None
        return layer

    def draw(self):
        if self.need_to_update:
            self._update()
        for layer in sorted(self.layers.keys()):
            self.layers[layer].draw()
