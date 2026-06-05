"""Players collection."""

from dataclasses import dataclass

from omok.model.player import Player
from omok.model.stone import Stone


@dataclass(frozen=True)
class Players:
    """Store turn order for the two players."""

    current_stone: Stone = Stone.BLACK

    def current(self) -> Player:
        """Return the player who should act now."""
        return Player(self.current_stone)

    def next_turn(self) -> "Players":
        """Return a new players object with the next stone selected."""
        return Players(self.current_stone.opponent())
