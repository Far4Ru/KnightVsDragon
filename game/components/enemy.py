import arcade


class Enemy:
    def __init__(self, sprites):
        self.sprite = arcade.Sprite(
            ":resources:images/animated_characters/male_person/malePerson_idle.png",
            center_x=1280 * 0.5,
            center_y=700,
            scale=0.5,
        )
        sprites.append(self.sprite)
