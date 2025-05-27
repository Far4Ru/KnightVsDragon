from dataclasses import dataclass

@dataclass
class Position:
    x: float
    y: float
class CollisionEvent(Event):
    entity_a: Entity
    entity_b: Entity

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
class Player:  # Маркерный компонент (без данных, но может иметь настройки)
    move_speed: float = 5.0
    jump_force: float = 10.0

@dataclass
class Enemy:
    enemy_type: str = "melee"  # "range", "boss"
    attack_cooldown: float = 2.0