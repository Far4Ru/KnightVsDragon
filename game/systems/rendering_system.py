import arcade
from pyglet.graphics import Batch
from pyglet.math import Vec2

from config import FONT_DEFAULT
from engine.core.system import system
from engine.engine import GameEngine
from game.components import Scale, Angle
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

    def update(self, entities):
        self.layers.clear()
        self.elements.clear()
        for entity in entities:
            layer_level = 0
            if Layer in entity.components:
                layer_level = entity.components[Layer].level
            scale = 1
            if Scale in entity.components:
                scale = entity.components[Scale].scale

            position = Vec2(0, 0)
            if Position in entity.components:
                position = entity.components[Position]

            angle = 0
            if Angle in entity.components:
                angle = entity.components[Angle].degree

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
            if Text in entity.components:
                if layer_level not in self.layers:
                    self.layers[layer_level] = Batch()
                batchLayer = self.layers[layer_level]
                if not isinstance(batchLayer, Batch):
                    print(f"Ошибка использования слоя для текста {entity.components[Text]}: "
                          f"{layer_level}")
                    continue
                text_button_config = entity.components[Text]
                text = arcade.Text(
                    text_button_config.text,
                    position.x, position.y,
                    text_button_config.color, text_button_config.font_size,
                    anchor_x="center",
                    anchor_y="center",
                    rotation=angle,
                    font_name=FONT_DEFAULT,
                    batch=batchLayer,
                )
                self.elements.append(text)

    def draw(self):
        for layer in sorted(self.layers.keys()):
            self.layers[layer].draw()
        self.batch.draw()
