"""Tests for the players collection."""

from omok.model.players import Players
from omok.model.stone import Stone


def test_current_returns_current_player() -> None:
    """Players should expose the player whose turn it is."""
    assert Players().current().stone is Stone.BLACK


def test_next_turn_switches_turn_order() -> None:
    """Players should move to the opposite stone after a turn."""
    assert Players().next_turn().current().stone is Stone.WHITE
