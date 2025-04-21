from abc import ABC, abstractmethod

class Event(ABC):
    pass

class TileSelectedEvent(Event):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class EventBus:
    def __init__(self):
        self._listeners = defaultdict(list)

    def subscribe(self, event_type, callback):
        self._listeners[event_type].append(callback)

    def post(self, event):
        for listener in self._listeners[type(event)]:
            listener(event)