from engine.engine import GameEngine
from game.views.menu_view import MenuView
from game.views.test_view import TestView


def main():
    engine = GameEngine()
    # engine.run(MenuView())
    engine.run(TestView())


if __name__ == "__main__":
    main()
