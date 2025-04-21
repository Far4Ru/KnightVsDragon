"""
Solitaire clone.
"""

import arcade

from src.GameWindow import GameWindow


def main():
    """Main function"""
    window = GameWindow()
    window.setup()
    arcade.run()

    # engine = GameEngine()
    # engine.run(MenuView())

if __name__ == "__main__":
    main()
