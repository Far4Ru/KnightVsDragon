from typing import Dict, List
from engine.core.system import system
from engine.core.system import System


@system
class TurnSystem(System):
    action_queue: List[Dict] = []
    waiting_for_animation = False

    def start(self, entities):
        def tile_select_wrapper(context):
            def tile_select(event):
                context.action_queue.append({
                    'type': 'tile_select',
                    'entity': event.entity,
                    'tile': event.tile,
                })
                pass
            return tile_select
        
        tile_select_callback = tile_select_wrapper(self)

        self.event_bus.subscribe("tile_select", self, tile_select_callback)

    def update(self, entities):
        if self.waiting_for_animation or not self.action_queue:
            return
        
        next_action = self.action_queue[0]
        if next_action['type'] == 'tile_select':
            entity = next_action['entity']
            self.action_queue.pop(0)
