SYSTEM_CLASSES = {}


def system(cls):
    SYSTEM_CLASSES[cls.__name__] = cls
    return cls
