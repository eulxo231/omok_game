"""Tests for the column label value object."""

import pytest

from omok.model.column_label import ColumnLabel
from omok.model.errors import InvalidPositionError


def test_zero_based_converts_column_text() -> None:
    """Column labels should convert to zero-based indices."""
    assert ColumnLabel("H").zero_based() == 7


def test_display_text_returns_normalized_label() -> None:
    """Column labels should normalize lowercase input."""
    assert ColumnLabel("h").display_text() == "H"


def test_invalid_column_raises_error() -> None:
    """Columns outside A to O should be rejected."""
    with pytest.raises(InvalidPositionError):
        ColumnLabel("P")
