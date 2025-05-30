from dataclasses import dataclass

from engine.core.component import component
from engine.core.action import action


@action
@component
@dataclass
class OnHover:
    is_hovered: bool = False
