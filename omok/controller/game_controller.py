"""Console game controller."""

from dataclasses import dataclass

from omok.controller.move_input_parser import MoveInputParser
from omok.model.errors import OmokError
from omok.model.game import Game
from omok.view.board_renderer import BoardRenderer
from omok.view.console_io import ConsoleIO


@dataclass
class GameController:
    """Coordinate the MVC components for console play."""

    game: Game
    parser: MoveInputParser
    renderer: BoardRenderer
    console: ConsoleIO

    @classmethod
    def create_default(cls) -> "GameController":
        """Build the default controller used by the application."""
        return cls(
            game=Game.start(),
            parser=MoveInputParser(),
            renderer=BoardRenderer(),
            console=ConsoleIO(),
        )

    def run(self) -> None:
        """Run the application loop until someone wins."""
        self.console.print_line("오목 게임을 시작합니다.")
        self._print_board()
        while not self.game.is_finished():
            self.console.print_line(self.game.turn_prompt())
            self._handle_turn()
        self.console.print_line(self.game.winner_message())

    def _handle_turn(self) -> None:
        """Handle one valid turn, retrying on invalid input."""
        try:
            move_text = self.console.read_line("위치를 입력하세요: ")
            position = self.parser.parse(move_text)
            self.game = self.game.apply_move(position)
            self._print_board()
        except OmokError as error:
            self.console.print_line(str(error))
            self._handle_turn()

    def _print_board(self) -> None:
        """Render the current board and print it."""
        self.console.print_line(self.renderer.render(self.game.board))
