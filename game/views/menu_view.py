from engine.core.scene import Scene


class MenuView(Scene):
    def __init__(self):
        super().__init__()
        # TODO: Add backround music

        # TODO: Add path lightning on hover
        # TODO: Add path darkening on disabled

        # TODO: Add path arrows to background
        
        # TODO: Add animation from top to final position

        # TODO: Add animated (looped) idle knight on the left
        # TODO: Add animated (looped) idle dragon on the right

        # TODO: Add settings button (sprite with text)
        # TODO: Add settings animation on mouse enter and leave: fullfilled
        # TODO: On settings click: bubbles with options (sound-, sound+)

        # TODO: On close: add background transition
        # TODO: On close: add character active animation and transition

        # Route: menu -> dialog1 -> level1 -> dialog2 -> level2 -> ... -> dialog6 -> win
        # Lose route: menu -> dialog1 -> level1 -> lose (restart)
        # Continue: menu (continue) -> dialog3 -> level3 -> ...
        # dialog -> menu
        # level -> menu
