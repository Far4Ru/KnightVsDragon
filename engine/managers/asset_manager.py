import json
import os

import arcade


class AssetManager:
    def __init__(self):
        self.textures = {}
        self.font_names = []
        self.sound_names = {}
        self.load_fonts()
        self.load_textures()
        self.load_sounds()
        
    def load_textures(self):
        folder_path = "assets/images"
        if not os.path.exists(folder_path):
            print(f"Папка {folder_path} не найдена!")
        for filename in os.listdir(folder_path):
            if filename.endswith(".png"):
                texture_name = filename[:-4]
                texture_path = os.path.join(folder_path, filename)

                self.textures[texture_name] = arcade.load_texture(texture_path)

    def get_texture(self, name):
        return self.textures[name]

    def load_sounds(self):
        folder_path = "assets/sounds"
        if not os.path.exists(folder_path):
            print(f"Папка {folder_path} не найдена!")
        for filename in os.listdir(folder_path):
            if filename.endswith(".mp3"):
                sound_name = filename[:-4]
                sound_path = os.path.join(folder_path, filename)
                arcade.load_sound(sound_path)
                self.sound_names[sound_name] = sound_path

    def get_sound(self, name):
        return self.sound_names[name]

    def load_level(self, level_id):
        path = f"assets/levels/level_{level_id}.json"
        with open(path) as f:
            return json.load(f)

    def load_fonts(self):
        folder_path = "assets/fonts"
        if not os.path.exists(folder_path):
            print(f"Папка {folder_path} не найдена!")
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".ttf"):
                font_name = os.path.splitext(filename)[0]
                font_path = os.path.join(folder_path, filename)
                arcade.load_font(font_path)
                self.font_names.append(font_name)
