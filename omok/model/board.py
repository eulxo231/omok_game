"""Board aggregate for omok."""

from dataclasses import dataclass, field

from omok.model.board_cells import BoardCells
from omok.model.direction import Direction
from omok.model.errors import InvalidMoveError
from omok.model.position import Position
from omok.model.stone import Stone


@dataclass
class Board:
    """Represent the omok board and its rules."""

    cells: BoardCells = field(default_factory=BoardCells)

    def place(self, position: Position, stone: Stone) -> None:
        """Place a stone at a validated and empty position."""
        if not self._is_inside(position.row_index(), position.column_index()):
            raise InvalidMoveError("보드 범위를 벗어난 위치입니다.")
        if not self.cells.is_empty_at(position.row_index(), position.column_index()):
            raise InvalidMoveError("이미 돌이 놓인 위치입니다.")
        self.cells.place(position.row_index(), position.column_index(), stone)

    def has_winning_line(self, position: Position, stone: Stone) -> bool:
        """Return whether the latest move created five or more stones in a row."""
        for direction in Direction.all_win_directions():
            if self._line_length(position, stone, direction) >= 5:
                return True
        return False

    def stone_at(self, row_index: int, column_index: int) -> Stone | None:
        """Return the stone at the requested zero-based coordinate."""
        return self.cells.stone_at(row_index, column_index)

    def _line_length(self, position: Position, stone: Stone, direction: Direction) -> int:
        """Count stones in both directions including the pivot stone."""
        return (
            1
            + self._count_one_side(position, stone, direction.row_step, direction.column_step)
            + self._count_one_side(position, stone, -direction.row_step, -direction.column_step)
        )

    def _count_one_side(
        self, position: Position, stone: Stone, row_step: int, column_step: int
    ) -> int:
        """Count consecutive stones for one traversal direction."""
        row_index, column_index = position.shifted(row_step, column_step)
        count = 0
        while self._is_inside(row_index, column_index):
            if self.stone_at(row_index, column_index) is not stone:
                return count
            count += 1
            row_index += row_step
            column_index += column_step
        return count

    def _is_inside(self, row_index: int, column_index: int) -> bool:
        """Return whether the coordinate exists on the board."""
        return 0 <= row_index < 15 and 0 <= column_index < 15
