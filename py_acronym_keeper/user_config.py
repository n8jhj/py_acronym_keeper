"""User configuration functionality."""

from pathlib import Path

from . import config
from .util import Stringer


class UserConfig:
    """Describes the user's configuration."""

    _default_file_path: Path = config.user_default_config_path()
    _repr_max_path_len: int = config.REPR_MAX_PATH_LEN
    assert _repr_max_path_len > 3

    def __init__(self, path: Path | None = None, parents: bool = False) -> None:
        """Creates an instance of UserConfig.

        Args:
            path: Path to configuration file. Default location is the user data
                dir.
            parents: Whether to create parent directories, if they don't exist.
                Default is false.
        """
        self._file_path: Path = self._default_file_path
        if path:
            self._file_path = path

        self.path.parent.mkdir(parents=parents, exist_ok=True)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({Stringer.truncate(str(self.path), self._repr_max_path_len)})"

    @property
    def path(self) -> Path:
        return self._file_path
