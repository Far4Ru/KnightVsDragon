from engine.engine import GameEngine
from game.views.menu_view import MenuView


def main():
    engine = GameEngine()
    engine.run(MenuView())

if __name__ == "__main__":
    main()
