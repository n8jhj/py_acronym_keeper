"""Defines functionality for printing acronyms to the console."""

from .acronym import Acronym, Pack


class Printer:
    # Seems reasonable.
    _default_max_line_length: int = 80
    # Replaces strings that are too long.
    _truncation_suffix: str = "..."
    # Enough for one letter and a truncation.
    _smallest_allowed_max_line_length: int = len(_truncation_suffix) + 1

    def __init__(self, max_line_length: int = _default_max_line_length) -> None:
        self.max_line_length = max_line_length

    @property
    def max_line_length(self) -> int:
        return self._max_line_length

    @max_line_length.setter
    def max_line_length(self, value: int) -> None:
        if value <= self._smallest_allowed_max_line_length:
            raise ValueError(f"Max line length {value} is too short")
        self._max_line_length = value

    def stringify_acronym(self, a: Acronym, max_len: int = -1) -> str:
        """Returns a single-line string representation of the given Acronym."""
        if max_len < 0:
            max_len = self.max_line_length
        line: str = f"{a.name} : {a.meaning} : {a.description}"
        if len(line) > max_len:
            trunc = self._truncation_suffix
            line = line[: max_len - len(trunc)] + trunc
        return line

    def stringify_pack(self, pack: Pack) -> str:
        """Returns a string representation of acronyms that can be printed."""
        result: str = ""
        for a in pack:
            result += self.stringify_acronym(a) + "\n"
        return result
