import arcade

import math

from pyglet.math import Vec2


def collides_with_point(rect: arcade.XYWH,
                        point: tuple[float | int, float | int] | Vec2,
                        angle: float = 0):
    position = Vec2(*point) if not isinstance(point, Vec2) else point
    local_x = position.x - rect.x
    local_y = position.y - rect.y

    angle_rad = math.radians(angle)
    rotated_x = local_x * math.cos(angle_rad) - local_y * math.sin(angle_rad)
    rotated_y = local_x * math.sin(angle_rad) + local_y * math.cos(angle_rad)

    return (
        -rect.width / 2 <= rotated_x <= rect.width / 2 and
        -rect.height / 2 <= rotated_y <= rect.height / 2
    )
