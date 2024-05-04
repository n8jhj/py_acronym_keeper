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

    def __repr__(self) -> str:
        return f"{type(self).__name__}(max_len={self.max_line_length})"

    @property
    def max_line_length(self) -> int:
        return self._max_line_length

    @max_line_length.setter
    def max_line_length(self, value: int) -> None:
        if not self.is_max_line_length_valid(value):
            raise ValueError(
                f"Max line length must be either < 0 or > {self._smallest_allowed_max_line_length}"
            )
        self._max_line_length = value

    @classmethod
    def is_max_line_length_valid(cls, value: int) -> bool:
        return value >= cls._smallest_allowed_max_line_length or value < 0

    def _truncate(self, s: str) -> str:
        if self.max_line_length >= 0 and len(s) > self.max_line_length:
            suffix = self._truncation_suffix
            return s[: self.max_line_length - len(suffix)] + suffix
        return s

    def stringify_acronym(self, a: Acronym) -> str:
        """Returns a single-line string representation of the given Acronym."""
        line: str = f"{a.name} : {a.meaning} : {a.description}"
        return self._truncate(line)

    def stringify_pack(self, pack: Pack) -> str:
        """Returns a string representation of acronyms that can be printed."""
        result: str = ""
        for a in pack:
            result += self.stringify_acronym(a) + "\n"
        return result
