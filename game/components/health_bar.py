import arcade
from pyglet.graphics import Batch


class HealthBar:
    def __init__(self, x, y, max_hp, current_hp, width=200, height=20):
        self.x = x
        self.y = y
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.batch = Batch()
        self.width = width
        self.height = height
        self.background_color = arcade.color.BLACK
        self.border_color = arcade.color.WHITE
        self.fill_color = arcade.color.GREEN
        self.text = arcade.Text(
            "",
            self.x, self.y,
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="center",
            batch=self.batch,
        )
        self.update_hp(current_hp)

    def draw(self):
        rect = arcade.Rect(self.x, self.x + self.width,
                           self.y, self.y + self.height,
                           self.width, self.height,
                           self.x, self.y)
        arcade.draw_rect_filled(
            rect,
            self.background_color
        )

        outline_rect = arcade.Rect(self.x - self.width * 0.5, self.x + self.width * 0.5,
                                   self.y - self.height * 0.5, self.y + self.height * 0.5,
                                   self.width, self.height,
                                   self.x - self.width * 0.5, self.y - self.height)
        arcade.draw_rect_outline(
            outline_rect,
            self.border_color, 2
        )

        health_width = max(0, (self.current_hp / self.max_hp) * self.width)

        filled_rect = arcade.Rect(self.x - (self.width - health_width) / 2, self.x + health_width,
                                  self.y, self.y + self.height, health_width, self.height,
                                  self.x - (self.width - health_width) / 2, self.y)
        if health_width > 0:
            arcade.draw_rect_filled(
                filled_rect,
                self.fill_color
            )

        self.text.text = f"{self.current_hp}/{self.max_hp}"
        self.batch.draw()

    def update_hp(self, current_hp):
        self.current_hp = current_hp
        self.current_hp = max(0, min(self.current_hp, self.max_hp))

        health_percent = self.current_hp / self.max_hp
        if health_percent < 0.2:
            self.fill_color = arcade.color.GREEN
        elif health_percent < 0.5:
            self.fill_color = arcade.color.ORANGE
        else:
            self.fill_color = arcade.color.RED
