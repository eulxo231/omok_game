"""Tests for the row number value object."""

import pytest

from omok.model.errors import InvalidPositionError
from omok.model.row_number import RowNumber


def test_zero_based_converts_row_number() -> None:
    """Row numbers should convert from display space to storage space."""
    assert RowNumber(8).zero_based() == 7


def test_display_text_returns_string_value() -> None:
    """Row numbers should render as text for prompts."""
    assert RowNumber(15).display_text() == "15"


def test_invalid_row_raises_error() -> None:
    """Rows outside 1 to 15 should be rejected."""
    with pytest.raises(InvalidPositionError):
        RowNumber(16)
