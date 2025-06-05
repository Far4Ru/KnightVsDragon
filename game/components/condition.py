from dataclasses import dataclass

from engine.core.component import component


def condition_any(self):
    def condition(*args):
        return True
    return condition


CONDITIONS = {
    "any": condition_any
}


@component
@dataclass
class Condition:
    check = None

    def __init__(self, name=None, args=None):
        if args is None:
            args = []

        if name in CONDITIONS:
            self.check = CONDITIONS[name](self, *args)
