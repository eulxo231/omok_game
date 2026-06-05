"""Console board renderer."""

from omok.model.board import Board


class BoardRenderer:
    """Render the board as text."""

    def render(self, board: Board) -> str:
        """Return the board string shown in the console."""
        lines = [self._render_row(board, row_number) for row_number in range(15, 0, -1)]
        lines.append("   " + "  ".join("ABCDEFGHIJKLMNO"))
        return "\n".join(lines)

    def _render_row(self, board: Board, row_number: int) -> str:
        """Return one rendered board row."""
        row_index = 15 - row_number
        pieces: list[str] = []
        for column_index in range(15):
            pieces.append(self._intersection(board, row_number, row_index, column_index))
            if column_index < 14:
                pieces.append("──")
        return f"{row_number:>2} " + "".join(pieces)

    def _intersection(
        self, board: Board, row_number: int, row_index: int, column_index: int
    ) -> str:
        """Return the symbol shown at one board intersection."""
        board_stone = board.stone_at(row_index, column_index)
        if board_stone is not None:
            return board_stone.symbol()
        return self._empty_intersection(row_number, column_index)

    def _empty_intersection(self, row_number: int, column_index: int) -> str:
        """Return the border character for an empty intersection."""
        if row_number == 15:
            return self._top_intersection(column_index)
        if row_number == 1:
            return self._bottom_intersection(column_index)
        return self._middle_intersection(column_index)

    def _top_intersection(self, column_index: int) -> str:
        """Return the top border intersection character."""
        if column_index == 0:
            return "┌"
        if column_index == 14:
            return "┐"
        return "┬"

    def _bottom_intersection(self, column_index: int) -> str:
        """Return the bottom border intersection character."""
        if column_index == 0:
            return "└"
        if column_index == 14:
            return "┘"
        return "┴"

    def _middle_intersection(self, column_index: int) -> str:
        """Return the middle row intersection character."""
        if column_index == 0:
            return "├"
        if column_index == 14:
            return "┤"
        return "┼"
