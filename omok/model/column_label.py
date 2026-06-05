"""Column label value object."""

from dataclasses import dataclass

from omok.model.errors import InvalidPositionError


@dataclass(frozen=True)
class ColumnLabel:
    """Wrap a board column label."""

    value: str

    def __post_init__(self) -> None:
        """Validate the column label after construction."""
        normalized = self.value.strip().upper()
        if len(normalized) != 1:
            raise InvalidPositionError("열은 A부터 O까지 한 글자여야 합니다.")
        if normalized < "A" or normalized > "O":
            raise InvalidPositionError("열은 A부터 O까지 입력해야 합니다.")
        object.__setattr__(self, "value", normalized)

    def zero_based(self) -> int:
        """Convert the column label to a zero-based index."""
        return ord(self.value) - ord("A")

    def display_text(self) -> str:
        """Return the normalized label text."""
        return self.value
