
MANAGERS = []


def manager(cls):
    MANAGERS.append(cls)
    return cls
