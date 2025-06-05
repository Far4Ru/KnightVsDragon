import arcade

from engine.engine import GameEngine
from engine.utils.math import hex_to_rgb


def action_exit(self):
    arcade.exit()


def action_change_scene(self, name="menu"):
    GameEngine().settings_manager.set("last_level", name)
    GameEngine().change_scene(name)


def action_continue(self):
    name = GameEngine().settings_manager.get("last_level")
    GameEngine().change_scene(name)


def action_change_color(self, hover_color, base_color):
    if self.target:
        if self.is_hovered:
            self.target.color = hex_to_rgb(hover_color)
        else:
            self.target.color = hex_to_rgb(base_color)


def action_sound_volume_plus(self):
    GameEngine().scene_manager.current_scene.event_bus.emit("sound_volume_plus", [])


def action_sound_volume_minus(self):
    GameEngine().scene_manager.current_scene.event_bus.emit("sound_volume_minus", [])


def action_change_slot_state(self):
    GameEngine().scene_manager.current_scene.event_bus.emit("change_slot_state", [])


ACTIONS = {
    "exit": action_exit,
    "change_scene": action_change_scene,
    "continue": action_continue,
    "change_color": action_change_color,
    "change_sound_volume_plus": action_sound_volume_plus,
    "change_sound_volume_minus": action_sound_volume_minus,
    "change_slot_state": action_change_slot_state,
}


def action(cls):
    if not hasattr(cls, 'action'):
        cls.action = None

    def __init__(self, action=None):
        func_name = action["name"]
        args = action.get("args", [])

        if func_name in ACTIONS:
            self.action = lambda: ACTIONS[func_name](self, *args)

    cls.__init__ = __init__
    return cls
