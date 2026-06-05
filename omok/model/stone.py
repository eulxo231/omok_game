"""Stone definitions used on the board."""

from enum import Enum


class Stone(Enum):
    """Represent a player's stone."""

    BLACK = ("흑", "●")
    WHITE = ("백", "○")

    def player_name(self) -> str:
        """Return the localized player name."""
        return self.value[0]

    def symbol(self) -> str:
        """Return the board symbol for the stone."""
        return self.value[1]

    def opponent(self) -> "Stone":
        """Return the opposing stone."""
        if self is Stone.BLACK:
            return Stone.WHITE
        return Stone.BLACK
