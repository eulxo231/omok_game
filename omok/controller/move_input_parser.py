"""Parse console move input."""

from omok.model.column_label import ColumnLabel
from omok.model.errors import InvalidPositionError
from omok.model.position import Position
from omok.model.row_number import RowNumber


class MoveInputParser:
    """Convert user input text into a position object."""

    def parse(self, text: str) -> Position:
        """Parse and validate position text such as H8."""
        normalized = text.strip().upper()
        if len(normalized) < 2:
            raise InvalidPositionError("위치는 열과 행을 함께 입력해야 합니다.")
        column_text = normalized[0]
        row_text = normalized[1:]
        if not row_text.isdigit():
            raise InvalidPositionError("행은 숫자로 입력해야 합니다.")
        return Position(ColumnLabel(column_text), RowNumber(int(row_text)))
