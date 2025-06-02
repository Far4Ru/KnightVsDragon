from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Tile:
    x: int = 0
    y: int = 0
    # original_texture: Optional[str] = None
    # current_texture: Optional[str] = None
