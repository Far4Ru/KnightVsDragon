from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Upgradable:
    current: int = 0

    def __init__(self, texture_names=None):
        self.texture_names = texture_names
