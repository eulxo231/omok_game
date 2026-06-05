"""Domain errors used by the omok model."""


class OmokError(Exception):
    """Base exception for omok domain errors."""


class InvalidMoveError(OmokError):
    """Raised when a move cannot be placed on the board."""


class InvalidPositionError(OmokError):
    """Raised when a position text or coordinate is invalid."""
