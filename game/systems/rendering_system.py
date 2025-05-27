import arcade

from engine.engine import GameEngine
from game.components.component import Layer, Position, Sprite

class RenderingSystem:
    def __init__(self, context):
        self.context = context
        self.sprite_lists = {}

    def update(self, entities):
        self.sprite_lists.clear()
        for entity in entities:            
            if Sprite in entity.components and Layer in entity.components:
                layer = entity.components[Layer].level
                if layer not in self.sprite_lists:
                    self.sprite_lists[layer] = arcade.SpriteList()
                
                sprite = arcade.Sprite(
                    GameEngine().texture_manager.get(entity.components[Sprite].texture),
                    center_x=entity.components[Position].x,
                    center_y=entity.components[Position].y,
                    scale=1,
                ) 
                self.sprite_lists[layer].append(sprite)

    def draw(self):
        for layer in sorted(self.sprite_lists.keys()):
            self.sprite_lists[layer].draw()