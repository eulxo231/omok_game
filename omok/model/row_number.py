"""Row number value object."""

from dataclasses import dataclass

from omok.model.errors import InvalidPositionError


@dataclass(frozen=True)
class RowNumber:
    """Wrap a board row number."""

    value: int

    def __post_init__(self) -> None:
        """Validate the row number after construction."""
        if self.value < 1 or self.value > 15:
            raise InvalidPositionError("행은 1부터 15까지 입력해야 합니다.")

    def zero_based(self) -> int:
        """Convert the row number to a zero-based index from the top."""
        return 15 - self.value

    def display_text(self) -> str:
        """Return the row text shown to the user."""
        return str(self.value)
