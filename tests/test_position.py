"""Tests for the position value object."""

from omok.model.column_label import ColumnLabel
from omok.model.position import Position
from omok.model.row_number import RowNumber


def test_row_index_returns_storage_row() -> None:
    """Positions should expose the row index used by the board."""
    position = Position(ColumnLabel("H"), RowNumber(8))
    assert position.row_index() == 7


def test_column_index_returns_storage_column() -> None:
    """Positions should expose the column index used by the board."""
    position = Position(ColumnLabel("H"), RowNumber(8))
    assert position.column_index() == 7


def test_shifted_returns_offset_coordinate() -> None:
    """Positions should support directional traversal."""
    position = Position(ColumnLabel("H"), RowNumber(8))
    assert position.shifted(1, -1) == (8, 6)


def test_display_text_returns_user_facing_text() -> None:
    """Positions should display as column plus row."""
    position = Position(ColumnLabel("H"), RowNumber(8))
    assert position.display_text() == "H8"
