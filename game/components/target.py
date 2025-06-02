from dataclasses import dataclass
from typing import Optional

from engine.core.component import component


@component
@dataclass
class Target:
    entity: Optional[str] = None
