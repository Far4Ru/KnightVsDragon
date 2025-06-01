import arcade


class ObjectFactory:
    def __init__(self, texture_manager):
        self.texture_manager = texture_manager

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

    def sprite(self, texture, position, scale, layer):
        sprite = arcade.Sprite(
            self.texture_manager.get(texture),
            center_x=position.x,
            center_y=position.y,
            scale=scale,
        )
        layer.append(sprite)
        return sprite

