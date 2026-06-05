"""Tests for the player value object."""

from omok.model.player import Player
from omok.model.stone import Stone


def test_prompt_text_without_last_move_mentions_turn_only() -> None:
    """The first prompt should not include a last move description."""
    assert Player(Stone.BLACK).prompt_text(None) == "흑의 차례입니다."


def test_prompt_text_with_last_move_mentions_position() -> None:
    """Subsequent prompts should show the previous move."""
    assert Player(Stone.WHITE).prompt_text("H8") == "백의 차례입니다. (마지막 돌의 위치: H8)"
