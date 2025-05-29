from dataclasses import dataclass

from engine.core.component import component
from game.components.action import Action


@component
@dataclass
class OnClick:
    action: Action = None
