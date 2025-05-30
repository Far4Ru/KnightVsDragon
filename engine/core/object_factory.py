import arcade


class ObjectFactory:
    @staticmethod
    def text(text, position, color, font_size, angle, font, batch_layer):
        return arcade.Text(
            text,
            position.x, position.y,
            color, font_size,
            anchor_x="center",
            anchor_y="center",
            rotation=angle,
            font_name=font,
            batch=batch_layer,
        )
