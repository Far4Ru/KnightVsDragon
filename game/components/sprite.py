from dataclasses import dataclass
from typing import Optional

from engine.core.component import component


@component
@dataclass
class Sprite:
    texture: str
    scale: float = 1.0
    visible: bool = True
    base_texture: Optional[str] = None

