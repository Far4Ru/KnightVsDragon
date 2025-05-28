from dataclasses import dataclass
from typing import Callable, Optional

import arcade

from engine.core.component import register_component

@dataclass
class Position:
    x: float
    y: float

@dataclass
class CharacterConfig:
    speed: float = 5.0
    jump_force: float = 10.0
    max_health: int = 100

@dataclass
class Health:
    current: int
    max: int

@dataclass
class Sprite:
    texture: str
    scale: float = 1.0
    
@dataclass
class Player:
    move_speed: float = 5.0
    jump_force: float = 10.0

@dataclass
class Enemy:
    enemy_type: str = "melee"  # "range", "boss"
    attack_cooldown: float = 2.0

@register_component
@dataclass
class Position:
    x: float
    y: float

@register_component
@dataclass
class Sprite:
    texture: str
    scale: float = 1.0
    
@register_component
@dataclass
class Layer:
    level: int



@register_component
@dataclass
class TextButton:
    text: str
    x: float
    y: float
    width: float = 200
    height: float = 50
    color: arcade.color = arcade.color.BLACK
    font_size: int = 20

@register_component
@dataclass
class Clickable:
    on_click: Callable[[], None]

@register_component
@dataclass
class ButtonState:
    is_hovered: bool = False
    normal_color: arcade.color = arcade.color.GRAY
    hover_color: arcade.color = arcade.color.BLUE

@register_component
@dataclass
class ButtonSound:
    click_sound: arcade.Sound

@register_component
@dataclass
class Action:
    execute: Callable[[], None]