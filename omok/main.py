"""Application entry point for the omok game."""

from omok.controller.game_controller import GameController


def main() -> None:
    """Run the console omok application."""
    GameController.create_default().run()


if __name__ == "__main__":
    main()
