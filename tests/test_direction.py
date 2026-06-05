"""Tests for traversal directions."""

from omok.model.direction import Direction


def test_all_win_directions_returns_four_axes() -> None:
    """Winning traversal should cover horizontal, vertical, and diagonals."""
    directions = Direction.all_win_directions()
    assert directions == (
        Direction(0, 1),
        Direction(1, 0),
        Direction(1, 1),
        Direction(1, -1),
    )
