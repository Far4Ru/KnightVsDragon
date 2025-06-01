import arcade

from engine.core.system import system, System
from engine.engine import GameEngine
from game.components.sound import Sound


@system
class SoundSystem(System):
    sounds = []

    def start(self, entities):
        self.sounds = []
        for entity in entities:
            if Sound in entity.components:
                soundName = entity.components[Sound].name
                isLoop = entity.components[Sound].loop
                sound = arcade.Sound(GameEngine().sound_manager.get(soundName), streaming=True)
                self.sounds.append(sound.play(loop=isLoop))

    def __del__(self):
        for sound in self.sounds:
            sound.delete()
        self.sounds.clear()
