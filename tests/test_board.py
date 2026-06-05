"""Tests for the board aggregate."""

import pytest

from omok.model.board import Board
from omok.model.column_label import ColumnLabel
from omok.model.errors import InvalidMoveError
from omok.model.position import Position
from omok.model.row_number import RowNumber
from omok.model.stone import Stone


def test_place_stores_stone_on_board() -> None:
    """Placed stones should be readable from the board."""
    board = Board()
    position = Position(ColumnLabel("H"), RowNumber(8))
    board.place(position, Stone.BLACK)
    assert board.stone_at(7, 7) is Stone.BLACK


def test_place_rejects_occupied_position() -> None:
    """The board should reject moves on occupied cells."""
    board = Board()
    position = Position(ColumnLabel("H"), RowNumber(8))
    board.place(position, Stone.BLACK)
    with pytest.raises(InvalidMoveError):
        board.place(position, Stone.WHITE)


def test_has_winning_line_detects_horizontal_five() -> None:
    """Five consecutive stones should win horizontally."""
    board = Board()
    positions = [
        Position(ColumnLabel("D"), RowNumber(8)),
        Position(ColumnLabel("E"), RowNumber(8)),
        Position(ColumnLabel("F"), RowNumber(8)),
        Position(ColumnLabel("G"), RowNumber(8)),
        Position(ColumnLabel("H"), RowNumber(8)),
    ]
    for position in positions:
        board.place(position, Stone.BLACK)
    assert board.has_winning_line(positions[-1], Stone.BLACK) is True


def test_has_winning_line_accepts_overline() -> None:
    """Six in a row should still count as a win."""
    board = Board()
    positions = [
        Position(ColumnLabel("D"), RowNumber(8)),
        Position(ColumnLabel("E"), RowNumber(8)),
        Position(ColumnLabel("F"), RowNumber(8)),
        Position(ColumnLabel("G"), RowNumber(8)),
        Position(ColumnLabel("H"), RowNumber(8)),
        Position(ColumnLabel("I"), RowNumber(8)),
    ]
    for position in positions:
        board.place(position, Stone.BLACK)
    assert board.has_winning_line(positions[-1], Stone.BLACK) is True
