import json
import os

import arcade

def load_asset_folder(name, ext):
    def decorator(func):
        def wrapper(*args, **kwargs):
            folder_path = f"assets/{name}"
            extension = f".{ext}"
            if not os.path.exists(folder_path):
                print(f"Папка {folder_path} не найдена!")
            for filename in os.listdir(folder_path):
                if (filename.endswith(extension)):
                    short_filename = filename[:-len(extension)]
                    file_path = os.path.join(folder_path, filename)
                    result = func(*args, short_filename, file_path)
            return result
        return wrapper
    return decorator


class AssetManager:
    def __init__(self, texture_manager, config_manager, sound_manager, font_manager):
        self.texture_manager = texture_manager
        self.config_manager = config_manager
        self.sound_manager = sound_manager
        self.font_manager = font_manager
        self.load_fonts()
        self.load_textures()
        self.load_sounds()
        self.load_configs()
        
    @load_asset_folder(name="images", ext="png")
    def load_textures(self, filename, file_path):
        self.texture_manager.add(filename, arcade.load_texture(file_path))

    @load_asset_folder(name="fonts", ext="ttf")
    def load_fonts(self, filename, file_path):
        arcade.load_font(file_path)
        self.font_manager.add(filename)

    @load_asset_folder(name="sounds", ext="mp3")
    def load_sounds(self, filename, file_path):
        self.sound_manager.add(filename, file_path)

    @load_asset_folder(name="configs", ext="json")
    def load_configs(self, filename, file_path):
        with open(file_path) as file:
            self.config_manager.add(filename, json.load(file))
