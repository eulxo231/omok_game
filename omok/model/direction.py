"""Direction value object used for line traversal."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Direction:
    """Represent a traversal direction on the board."""

    row_step: int
    column_step: int

    @classmethod
    def all_win_directions(cls) -> tuple["Direction", ...]:
        """Return the directions that can produce a winning line."""
        return (
            cls(0, 1),
            cls(1, 0),
            cls(1, 1),
            cls(1, -1),
        )
