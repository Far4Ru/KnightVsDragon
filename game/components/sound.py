from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Sound:
    name: str
    loop: bool = True
