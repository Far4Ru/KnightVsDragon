import arcade
import math

from config import FONT_DEFAULT


class MenuButton:
    def __init__(self, batch, text="", x=0, y=0, width=0, height=0, angle=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.text = arcade.Text(
            text,
            self.x, self.y,
            arcade.color.BLACK,
            18,
            anchor_x="center",
            anchor_y="center",
            rotation=self.angle,
            font_name=FONT_DEFAULT,
            batch=batch,
        )

    def collides_with_point(self, x, y):
        local_x = x - self.x
        local_y = y - self.y

        angle_rad = math.radians(self.angle)
        rotated_x = local_x * math.cos(angle_rad) - local_y * math.sin(angle_rad)
        rotated_y = local_x * math.sin(angle_rad) + local_y * math.cos(angle_rad)

        return (
            -self.width / 2 <= rotated_x <= self.width / 2 and
            -self.height / 2 <= rotated_y <= self.height / 2
        )

    def on_mouse_motion(self, x, y):
        if self.collides_with_point(x, y):
            self.enter()
        else:
            self.leave()

    def enter(self):
        self.text.color = arcade.color.GREEN

    def leave(self):
        self.text.color = arcade.color.BLACK

