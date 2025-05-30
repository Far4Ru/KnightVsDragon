import arcade

from engine.core.system import system
from engine.engine import GameEngine
from game.components.sound import Sound


@system
class SoundSystem:
    def __init__(self, context):
        self.context = context
        self.sounds = []

    def update(self, entities):
        # for entity in entities:
        #     if Sound in entity.components:
        #         soundName = entity.components[Sound].name
        #         isLoop = entity.components[Sound].loop
        #         sound = arcade.Sound(GameEngine().sound_manager.get(soundName), streaming=True)
        #         sound.play(loop=isLoop)
        #         self.sounds.append(sound)
        pass
