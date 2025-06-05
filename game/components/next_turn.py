from dataclasses import dataclass
from typing import Optional

from engine.core.component import component


@component
@dataclass
class NextTurn:
    next: Optional[int] = None
