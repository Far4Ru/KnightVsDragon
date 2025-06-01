from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Grid:
    cols: int
    rows: int
    cell_size: int
    texture: str
