import arcade

from engine.core.system import system, System
from engine.engine import GameEngine
from game.components.sound import Sound


@system
class SoundSystem(System):
    sounds = []
    volume: float = 1.0

    def start(self, entities):
        self.sounds = []
        for entity in entities:
            if sound := entity.get_component(Sound):
                playable_sound = arcade.Sound(GameEngine().sound_manager.get(sound.name), streaming=True)
                player = playable_sound.play(loop=sound.loop)
                self.sounds.append(player)

        def change_sound_volume_wrapper(context, dv):
            def sound_volume_change(event=None):
                context.change_sound_volume(dv)
            return sound_volume_change

        self.event_bus.subscribe("sound_volume_plus", self, change_sound_volume_wrapper(self, 0.1))
        self.event_bus.subscribe("sound_volume_minus", self, change_sound_volume_wrapper(self, -0.1))

    def change_sound_volume(self, dv):
        self.volume += dv
        for sound_player in self.sounds:
            sound_player.volume = self.volume

    def __del__(self):
        for sound in self.sounds:
            sound.delete()
        self.sounds.clear()
