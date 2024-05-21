import pytest

from py_acronym_keeper.util import Stringer


@pytest.mark.parametrize(
    ["s", "max_len", "suffix", "expected"],
    [
        ("abcde", 2, "...", ValueError),
        ("abcde", 3, "...", ValueError),
        ("abcde", 4, "...", "a..."),
    ],
)
def test_truncate(s: str, max_len: int, suffix: str, expected: str | type) -> None:
    if isinstance(expected, str):
        assert Stringer.truncate(s, max_len, suffix=suffix) == expected
    elif issubclass(expected, Exception):
        with pytest.raises(expected) as e:
            Stringer.truncate(s, max_len, suffix=suffix)
    else:
        assert False, "Bad type for test case."
