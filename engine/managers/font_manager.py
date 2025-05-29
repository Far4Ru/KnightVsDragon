
from engine.core.manager import manager


@manager
class FontManager:
    def __init__(self):
        self.fonts = []

    def add(self, font_name):
        self.fonts.append(font_name)
