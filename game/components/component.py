from dataclasses import dataclass

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