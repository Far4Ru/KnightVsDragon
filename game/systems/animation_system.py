import copy
from engine.core.system import system, System
from game.components import Target, Turn
from game.components.animation import Animation


def wrapper_add_animation(self, entities):
    def add_animation(event):
        print(event)
        self.animations.append(event)
    return add_animation

@system
class AnimationSystem(System):
    animations = []

    def start(self, entities):
        self.animations.clear()

        self.event_bus.subscribe("add_animation", self, wrapper_add_animation(self, entities))
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
        # for entity in entities:
        #     if animation := entity.get_component(Animation):
        #         if animation.active:
        #             animation.dt = dt
        #             animation.update()
        for animation in self.animations:
            if animation.active:
                animation.dt = dt
                animation.update()

