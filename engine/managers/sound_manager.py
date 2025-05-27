class SoundManager:
    def __init__(self):
        self.sounds = {}

    def add(self, sound_name, file_path):
        self.sounds[sound_name] = file_path

    def get(self, sound_name):
        return self.sounds[sound_name]