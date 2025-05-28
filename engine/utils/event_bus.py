import arcade
from typing import Dict, List, Callable, Any, Set
from collections import defaultdict

class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, Dict[object, List[Callable[[Any], None]]]] = defaultdict(lambda: defaultdict(list))
        self._event_queue: List[tuple[str, Any]] = []
        self._processing_events: Set[str] = set()

    def subscribe(self, event_type: str, subscriber: object, callback: Callable[[Any], None]):
        self._subscribers[event_type][subscriber].append(callback)

    def unsubscribe(self, event_type: str, subscriber: object):
        if event_type in self._subscribers and subscriber in self._subscribers[event_type]:
            del self._subscribers[event_type][subscriber]

    def unsubscribe_all(self, subscriber: object):
        for event_type in self._subscribers:
            if subscriber in self._subscribers[event_type]:
                del self._subscribers[event_type][subscriber]

    def emit(self, event_type: str, event_data: Any = None):
        self._event_queue.append((event_type, event_data))

    def process(self):
        current_events = self._event_queue.copy()
        self._event_queue.clear()
        
        for event_type, event_data in current_events:
            if event_type in self._processing_events:
                continue
            self._processing_events.add(event_type)
            subscribers = self._subscribers.get(event_type, {})
            for subscriber, callbacks in subscribers.items():
                for callback in callbacks:
                    try:
                        callback(event_data)
                    except Exception as e:
                        arcade.log(f"Ошибка обработка события {event_type}: {e}")
            self._processing_events.remove(event_type)

    def clear(self):
        self._subscribers.clear()
        self._event_queue.clear()
        self._processing_events.clear()