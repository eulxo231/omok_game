"""Tests for parsing move input."""

import pytest

from omok.controller.move_input_parser import MoveInputParser
from omok.model.errors import InvalidPositionError


def test_parse_returns_position_for_valid_text() -> None:
    """Valid text should be parsed into a displayable position."""
    assert MoveInputParser().parse("h8").display_text() == "H8"


def test_parse_rejects_text_without_row_digits() -> None:
    """Moves should include a numeric row value."""
    with pytest.raises(InvalidPositionError):
        MoveInputParser().parse("HA")
