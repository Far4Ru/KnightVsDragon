import arcade


class Player:
    def __init__(self, sprites):
        self.sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_person/femalePerson_idle.png",
            center_x=1280 * 0.5,
            center_y=100,
        )
        sprites.append(self.sprite)
