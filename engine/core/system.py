SYSTEM_CLASSES = {}


def system(cls):
    SYSTEM_CLASSES[cls.__name__] = cls
    return cls


def get_entity_value(entity, entity_class):
    if entity_class in entity.components:
        return entity.components[entity_class]
    return entity_class()
