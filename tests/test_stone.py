"""Tests for the stone enum."""

from omok.model.stone import Stone


def test_player_name_returns_korean_name() -> None:
    """Stone should expose the player name used in prompts."""
    assert Stone.BLACK.player_name() == "흑"


def test_symbol_returns_board_symbol() -> None:
    """Stone should expose the symbol used on the board."""
    assert Stone.WHITE.symbol() == "○"


def test_opponent_returns_opposite_stone() -> None:
    """Stone should return the opposing turn value."""
    assert Stone.BLACK.opponent() is Stone.WHITE
