import arcade
from pyglet.graphics import Batch

from config import FONT_DEFAULT
from engine.core.system import system, System
from engine.engine import GameEngine
from engine.utils.math import calculate_perspective_scale
from game.components import Scale, Angle, Grid
from game.components.droppable import Droppable
from game.components.layer import Layer
from game.components.position import Position
from game.components.sprite import Sprite
from game.components.text import Text


@system
class RenderingSystem(System):
    layers = {}
    batch = Batch()
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
                angle = entity.get_component(Angle).degree
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
                self.elements.append(text)
                continue
        self.need_to_update = False

    def draw(self):
        if self.need_to_update:
            self._update()
        for layer in sorted(self.layers.keys()):
            self.layers[layer].draw()
        self.batch.draw()
