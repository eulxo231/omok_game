"""Console input and output helpers."""


class ConsoleIO:
    """Handle console communication."""

    def print_line(self, message: str) -> None:
        """Print one line to standard output."""
        print(message)

    def read_line(self, prompt: str) -> str:
        """Read one line from standard input."""
        return input(prompt)
