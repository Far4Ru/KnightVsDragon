import arcade

from engine.engine import GameEngine
from game.components.sound import Sound


class SoundSystem:
    def __init__(self, context):
        self.context = context
        self.sounds = []
        # for entity in context.entities:
        #     if Sound in entity.components:
        #         soundName = entity.components[Sound].name
        #         isLoop = entity.components[Sound].loop
        #         sound = arcade.Sound(GameEngine().sound_manager.get(soundName), streaming=True)
        #         sound.play(loop=isLoop)
        #         self.sounds.append(sound)
