import arcade


class ObjectFactory:
    def __init__(self, texture_manager):
        self.texture_manager = texture_manager

    @staticmethod
    def text(text, position, color, font_size, angle, font, batch_layer, width=None, multiline=False, anchor_x="center",
             anchor_y="center"):
        return arcade.Text(
            text,
            position.x, position.y,
            color, font_size,
            width=width,
            multiline=multiline,
            anchor_x=anchor_x,
            anchor_y=anchor_y,
            rotation=angle,
            font_name=font,
            batch=batch_layer,
        )

    # def rectangle(self):
    #         texture = arcade.rect("rect", (width, height), color)
    #         sprite = arcade.Sprite()
    #         sprite.texture = texture
    #         return sprite

    def sprite(self, texture, position, scale, layer, angle=0):
        sprite = arcade.Sprite(
            self.texture_manager.get(texture),
            center_x=position.x,
            center_y=position.y,
            scale=scale,
            angle=angle
        )
        layer.append(sprite)
        return sprite
