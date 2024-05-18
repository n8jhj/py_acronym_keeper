import pytest

from py_acronym_keeper.util import Stringer


@pytest.mark.parametrize(
    ["s", "max_len", "suffix", "expected"],
    [
        ("abcdefghijkl", 5, "...", "ab..."),
    ],
)
def test_truncate(s: str, max_len: int, suffix: str, expected: str) -> None:
    assert Stringer.truncate(s, max_len, suffix=suffix) == expected
