"""Game aggregate coordinating board state and turn state."""

from dataclasses import dataclass, replace

from omok.model.board import Board
from omok.model.players import Players
from omok.model.position import Position
from omok.model.stone import Stone


@dataclass(frozen=True)
class Game:
    """Represent the whole game state."""

    board: Board
    players: Players
    winner: Stone | None = None
    last_position: Position | None = None

    @classmethod
    def start(cls) -> "Game":
        """Create a new game with an empty board."""
        return cls(board=Board(), players=Players())

    def turn_prompt(self) -> str:
        """Return the prompt text for the current player."""
        last_position_text = None
        if self.last_position is not None:
            last_position_text = self.last_position.display_text()
        return self.players.current().prompt_text(last_position_text)

    def apply_move(self, position: Position) -> "Game":
        """Return the next game state after a valid move."""
        current_player = self.players.current()
        self.board.place(position, current_player.stone)
        if self.board.has_winning_line(position, current_player.stone):
            return replace(self, winner=current_player.stone, last_position=position)
        return replace(
            self,
            players=self.players.next_turn(),
            last_position=position,
        )

    def is_finished(self) -> bool:
        """Return whether the game already has a winner."""
        return self.winner is not None

    def winner_message(self) -> str:
        """Return the winner announcement shown to the user."""
        if self.winner is None:
            return ""
        return f"{self.winner.player_name()}이 승리했습니다."
