"""Tests for board rendering."""

from omok.model.board import Board
from omok.model.column_label import ColumnLabel
from omok.model.position import Position
from omok.model.row_number import RowNumber
from omok.model.stone import Stone
from omok.view.board_renderer import BoardRenderer


def test_render_returns_board_with_axis_labels() -> None:
    """An empty board render should include board coordinates."""
    rendered = BoardRenderer().render(Board())
    assert "A  B  C  D  E  F  G  H  I  J  K  L  M  N  O" in rendered


def test_render_shows_placed_stone_symbol() -> None:
    """Rendered boards should display placed stones."""
    board = Board()
    board.place(Position(ColumnLabel("H"), RowNumber(8)), Stone.BLACK)
    rendered = BoardRenderer().render(board)
    assert "●" in rendered


def test_render_keeps_board_shape_when_stone_is_placed() -> None:
    """A placed stone should replace an intersection without breaking the row shape."""
    board = Board()
    board.place(Position(ColumnLabel("H"), RowNumber(8)), Stone.BLACK)
    rendered_lines = BoardRenderer().render(board).splitlines()
    assert rendered_lines[7] == " 8 ├──┼──┼──┼──┼──┼──┼──●──┼──┼──┼──┼──┼──┼──┤"
