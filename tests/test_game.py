"""Tests for the game aggregate."""

from omok.model.column_label import ColumnLabel
from omok.model.game import Game
from omok.model.position import Position
from omok.model.row_number import RowNumber
from omok.model.stone import Stone


def test_start_creates_unfinished_game() -> None:
    """A new game should start without a winner."""
    assert Game.start().is_finished() is False


def test_turn_prompt_shows_first_player() -> None:
    """The opening prompt should mention the black player."""
    assert Game.start().turn_prompt() == "흑의 차례입니다."


def test_apply_move_switches_turn_and_tracks_last_position() -> None:
    """Valid moves should update turn order and last move text."""
    game = Game.start()
    next_game = game.apply_move(Position(ColumnLabel("H"), RowNumber(8)))
    assert next_game.turn_prompt() == "백의 차례입니다. (마지막 돌의 위치: H8)"


def test_apply_move_marks_winner() -> None:
    """The game should finish when the latest move creates a line."""
    game = Game.start()
    black_positions = ["D8", "E8", "F8", "G8", "H8"]
    white_positions = ["A1", "A2", "A3", "A4"]
    move_texts = [
        black_positions[0],
        white_positions[0],
        black_positions[1],
        white_positions[1],
        black_positions[2],
        white_positions[2],
        black_positions[3],
        white_positions[3],
        black_positions[4],
    ]
    for move_text in move_texts:
        game = game.apply_move(_position_from_text(move_text))
    assert game.winner is Stone.BLACK


def test_winner_message_returns_localized_message() -> None:
    """Finished games should expose a winner message."""
    game = Game.start()
    black_positions = ["D8", "E8", "F8", "G8", "H8"]
    white_positions = ["A1", "A2", "A3", "A4"]
    move_texts = [
        black_positions[0],
        white_positions[0],
        black_positions[1],
        white_positions[1],
        black_positions[2],
        white_positions[2],
        black_positions[3],
        white_positions[3],
        black_positions[4],
    ]
    for move_text in move_texts:
        game = game.apply_move(_position_from_text(move_text))
    assert game.winner_message() == "흑이 승리했습니다."


def _position_from_text(text: str) -> Position:
    """Create a position from compact test text."""
    return Position(ColumnLabel(text[0]), RowNumber(int(text[1:])))
