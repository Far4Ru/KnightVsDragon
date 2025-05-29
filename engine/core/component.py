COMPONENT_CLASSES = {}


def component(cls):
    COMPONENT_CLASSES[cls.__name__] = cls
    return cls
