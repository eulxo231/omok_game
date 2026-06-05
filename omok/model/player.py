"""Player value object."""

from dataclasses import dataclass

from omok.model.stone import Stone


@dataclass(frozen=True)
class Player:
    """Represent a player taking turns."""

    stone: Stone

    def prompt_text(self, last_position_text: str | None) -> str:
        """Build the turn prompt shown to the user."""
        if last_position_text is None:
            return f"{self.stone.player_name()}의 차례입니다."
        return (
            f"{self.stone.player_name()}의 차례입니다. "
            f"(마지막 돌의 위치: {last_position_text})"
        )
