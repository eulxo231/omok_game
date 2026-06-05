"""Tests for the game controller."""

from dataclasses import dataclass, field

from omok.controller.game_controller import GameController
from omok.controller.move_input_parser import MoveInputParser
from omok.model.game import Game
from omok.view.board_renderer import BoardRenderer


@dataclass
class FakeConsole:
    """Test double that records console output."""

    inputs: list[str]
    outputs: list[str] = field(default_factory=list)

    def print_line(self, message: str) -> None:
        """Record printed messages for assertions."""
        self.outputs.append(message)

    def read_line(self, prompt: str) -> str:
        """Return the next scripted input."""
        self.outputs.append(prompt)
        return self.inputs.pop(0)


def test_create_default_builds_working_components() -> None:
    """The default factory should wire the concrete MVC parts."""
    controller = GameController.create_default()
    assert isinstance(controller.parser, MoveInputParser)


def test_run_finishes_when_someone_wins() -> None:
    """The controller should announce the winner after a valid sequence."""
    console = FakeConsole(["D8", "A1", "E8", "A2", "F8", "A3", "G8", "A4", "H8"])
    controller = GameController(
        game=Game.start(),
        parser=MoveInputParser(),
        renderer=BoardRenderer(),
        console=console,
    )
    controller.run()
    assert console.outputs[-1] == "흑이 승리했습니다."
