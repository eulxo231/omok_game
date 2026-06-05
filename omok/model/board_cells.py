"""First-class collection for board cells."""

from dataclasses import dataclass, field

from omok.model.stone import Stone


@dataclass
class BoardCells:
    """Store the stones placed on the omok board."""

    rows: list[list[Stone | None]] = field(
        default_factory=lambda: [[None for _ in range(15)] for _ in range(15)]
    )

    def is_empty_at(self, row_index: int, column_index: int) -> bool:
        """Return whether the target cell is empty."""
        return self.rows[row_index][column_index] is None

    def place(self, row_index: int, column_index: int, stone: Stone) -> None:
        """Store a stone at the given coordinates."""
        self.rows[row_index][column_index] = stone

    def stone_at(self, row_index: int, column_index: int) -> Stone | None:
        """Return the stone stored at the given coordinates."""
        return self.rows[row_index][column_index]
