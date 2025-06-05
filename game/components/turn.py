from dataclasses import dataclass
from typing import Optional

from engine.core.component import component


@component
@dataclass
class Turn:
    order: int = 0
    current: bool = False
    next: Optional[int] = None
