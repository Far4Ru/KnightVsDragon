import copy
from engine.core.system import system, System
from game.components import Target
from game.components.animation import Animation


@system
class AnimationSystem(System):
    animations = []

    def start(self, entities):
        self.animations.clear()
        for entity in entities:
            if animation := entity.get_component(Animation):
                if target := entity.get_component(Target):
                    if target_entity := next((x for x in entities if x.type == target.entity), None):
                        if target.copy:
                            animation.target = copy.deepcopy(target_entity)
                        else:
                            animation.target = target_entity
                if animation.event is not None:
                    self.event_bus.subscribe(animation.event, entity, animation.init)
                else:
                    animation.init()
                self.animations.append(animation)

    def on_update(self, entities, dt):
        for animation in self.animations:
            if animation.active:
                animation.dt = dt
                animation.update()

