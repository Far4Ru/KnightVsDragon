class TextureManager:
    def __init__(self):
        self.textures = {}

    def add(self, texture_name, texture):
        self.textures[texture_name] = texture

    def get(self, texture_name):
        return self.textures[texture_name]
