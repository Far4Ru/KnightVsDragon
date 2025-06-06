from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Damage:
    def __init__(self, value=0):
        self.value = value
