"""Tests for the board cell collection."""

from omok.model.board_cells import BoardCells
from omok.model.stone import Stone


def test_is_empty_at_returns_true_for_new_board() -> None:
    """Newly created boards should start empty."""
    assert BoardCells().is_empty_at(0, 0) is True


def test_place_stores_stone() -> None:
    """Placing a stone should store it in the collection."""
    cells = BoardCells()
    cells.place(0, 0, Stone.BLACK)
    assert cells.stone_at(0, 0) is Stone.BLACK


def test_stone_at_returns_none_for_empty_cell() -> None:
    """Empty cells should expose the absence of a stone."""
    assert BoardCells().stone_at(3, 3) is None
