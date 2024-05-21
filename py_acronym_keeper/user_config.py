"""User configuration functionality."""

from collections.abc import Iterable, MutableMapping
from pathlib import Path
from typing import Any

import tomlkit

from . import config
from .util import Stringer


class UserConfigVariables(MutableMapping):
    __slots__ = ("store_path",)

    def __init__(self, values: dict[str, Any]) -> None:
        for k, v in values.items():
            setattr(self, k, v)

    def __getitem__(self, name: str) -> Any:
        return getattr(self, name)

    def __setitem__(self, name: str, value: Any) -> None:
        setattr(self, name, value)

    def __delitem__(self, name: str) -> None:
        delattr(self, name)

    def __iter__(self) -> Iterable:
        return ((k, getattr(self, k)) for k in self.__slots__ if hasattr(self, k))

    def __len__(self) -> int:
        count: int = 0
        for k in self.__slots__:
            if hasattr(self, k):
                count += 1
        return count


class UserConfig:
    """Describes the user's configuration."""

    _default_file_path: Path = config.user_default_config_path()
    _repr_max_path_len: int = config.REPR_MAX_PATH_LEN
    assert _repr_max_path_len > 3

    def __init__(
        self,
        path: Path | None = None,
        variables: dict[str, Any] | None = None,
        parents: bool = False,
    ) -> None:
        """Creates an instance of UserConfig.

        Args:
            path: Path to configuration file. Default location is the user data
                dir.
            variables: MutableMapping of variable names to values. Default is
                None.
            parents: Whether to create parent directories for the config file,
                if they don't exist. Default is false.
        """
        self._file_path: Path = self._default_file_path
        if path:
            self._file_path = path

        self.path.parent.mkdir(parents=parents, exist_ok=True)

        if not variables:
            variables = {}
        self._variables: UserConfigVariables = UserConfigVariables(variables)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({Stringer.truncate(str(self.path), self._repr_max_path_len, tail=True)})"

    @property
    def path(self) -> Path:
        return self._file_path

    @path.setter
    def path(self, value: Path) -> None:
        self._file_path = value

    def set_variable(self, name: str, value: Any) -> None:
        try:
            self._variables[name] = value
        except AttributeError:
            raise ValueError(f"Unrecognized variable {name!r}")

        # self.write()

    def write(self) -> None:
        doc = tomlkit.document()
        for k, v in self._variables.items():
            doc.append(k, v)
