import arcade
from pyglet.graphics import Batch

from config import FONT_DEFAULT
from engine.engine import GameEngine
from game.components.layer import Layer
from game.components.sprite import Sprite, Position
from game.components.text_button import Text


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
            if Sprite in entity.components and Layer in entity.components:
                layer = entity.components[Layer].level
                if layer not in self.layers:
                    self.layers[layer] = arcade.SpriteList()

                sprite = arcade.Sprite(
                    GameEngine().texture_manager.get(entity.components[Sprite].texture),
                    center_x=entity.components[Position].x,
                    center_y=entity.components[Position].y,
                    scale=1,
                )
                self.layers[layer].append(sprite)
            if Text in entity.components:
                layer = entity.components[Layer].level
                if layer not in self.layers:
                    self.layers[layer] = Batch()
                batchLayer = self.layers[layer]
                if not isinstance(batchLayer, Batch):
                    print(f"Ошибка использования слоя для текста {entity.components[Text]}: "
                          f"{layer}")
                    continue
                text_button_config = entity.components[Text]
                position = entity.components[Position]
                angle = 0
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
