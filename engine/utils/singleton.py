def singleton(cls):
    if not hasattr(cls, '_instance'):
        cls._instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super(self.__class__, self).__new__(self)
            self._instance._init()
        return self._instance

    cls.__new__ = __new__
    return cls
