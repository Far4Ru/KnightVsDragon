from dataclasses import dataclass

from engine.core.component import component


@component
@dataclass
class Droppable:
    droppable = True
