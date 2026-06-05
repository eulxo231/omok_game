"""Board position value object."""

from dataclasses import dataclass

from omok.model.column_label import ColumnLabel
from omok.model.row_number import RowNumber


@dataclass(frozen=True)
class Position:
    """Represent a validated board position."""

    column: ColumnLabel
    row: RowNumber

    def row_index(self) -> int:
        """Return the zero-based row index for storage."""
        return self.row.zero_based()

    def column_index(self) -> int:
        """Return the zero-based column index for storage."""
        return self.column.zero_based()

    def shifted(self, row_step: int, column_step: int) -> tuple[int, int]:
        """Return a shifted zero-based coordinate for traversal."""
        return self.row_index() + row_step, self.column_index() + column_step

    def display_text(self) -> str:
        """Return the display text used in prompts."""
        return f"{self.column.display_text()}{self.row.display_text()}"
