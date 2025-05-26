from enum import Enum

import arcade
from pyglet.graphics import Batch


class LayerType(Enum):
    DEFAULT = 0
    SPRITE = 1
    BATCH = 2


class DefaultLayer:
    def draw(self):
        pass


class Layers:
    def __init__(self):
        self.list = {}

    def add_layer(self, layer_name, layer_type=LayerType.SPRITE, default_layer=DefaultLayer):
        if layer_type == LayerType.SPRITE:
            self.list[layer_name] = arcade.SpriteList()
        elif layer_type == LayerType.BATCH:
            self.list[layer_name] = Batch()
        elif layer_type == LayerType.DEFAULT:
            self.list[layer_name] = default_layer()

    def add(self, layer_name, item):
        layer = self.list[layer_name]
        if isinstance(layer, arcade.SpriteList):
            layer.append(item)

    def get(self, layer_name):
        return self.list[layer_name]

    def draw(self):
        for layer in self.list.values():
            layer.draw()
