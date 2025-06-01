SYSTEM_CLASSES = {}


def system(cls):
    SYSTEM_CLASSES[cls.__name__] = cls
    return cls


class System:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.setup()

    def setup(self):
        pass
