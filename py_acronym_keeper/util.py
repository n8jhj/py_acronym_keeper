"""Defines various utilities."""


class Stringer:
    """Handles various string operations."""

    @staticmethod
    def truncate(s: str, max_len: int, suffix: str = "...", tail: bool = False) -> str:
        if max_len <= len(suffix):
            raise ValueError(f"max_len ({max_len}) < len(suffix) ({len(suffix)})")

        if max_len >= 0 and len(s) > max_len:
            if not tail:
                return s[: max_len - len(suffix)] + suffix
            else:
                return suffix + s[-(max_len - len(suffix)) :]
        return s
