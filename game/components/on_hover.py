from dataclasses import dataclass

from engine.core.component import component
from game.utils.action import action


@action
@component
@dataclass
class OnHover:
    target = None
    is_hovered: bool = False
