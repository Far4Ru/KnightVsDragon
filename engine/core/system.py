SYSTEM_CLASSES = {}


def system(cls):
    SYSTEM_CLASSES[cls.__name__] = cls
    return cls


def get_entity_value(entity, entity_class):
    if entity_class in entity.components:
        return entity.components[entity_class]
    return entity_class()


class System:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.setup()

    def setup(self):
        pass
