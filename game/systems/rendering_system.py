import arcade
from pyglet.graphics import Batch

from config import FONT_DEFAULT
from engine.core.system import system, System
from engine.engine import GameEngine
from game.components import Scale, Angle
from game.components.health import Health
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
            if entity.has_component(Health):
                #     self.batch = Batch()
                #     self.width = width
                #     self.height = height
                #     self.background_color = arcade.color.BLACK
                #     self.border_color = arcade.color.WHITE
                #     self.fill_color = arcade.color.GREEN
                #     self.text = arcade.Text(
                #         "",
                #         self.x, self.y,
                #         arcade.color.WHITE, 12,
                #         anchor_x="center", anchor_y="center",
                #         batch=self.batch,
                #     )
                #     self.update_hp(current_hp)
                continue
            if Sprite in entity.components:
                spriteLayer = self.get_layer(layer_level)
                if spriteLayer is None:
                    continue
                GameEngine().add.sprite(entity.components[Sprite].texture, position, scale, spriteLayer)
                continue
            if Text in entity.components:
                angle = entity.get_component(Angle).degree
                batchLayer = self.get_layer(layer_level, Batch)
                if batchLayer is None:
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
        self.batch.draw()
