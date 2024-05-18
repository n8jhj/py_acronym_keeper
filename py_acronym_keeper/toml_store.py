"""Handles TOML file storage."""

from pathlib import Path

import tomlkit

from . import config
from .acronym import Acronym, Pack
from .util import Stringer


class TOMLStore:
    """Describes the TOML structure used for storing acronyms."""

    _default_file_path: Path = config.user_default_store_path()
    _repr_max_path_len: int = config.REPR_MAX_PATH_LEN
    assert _repr_max_path_len > 3

    def __init__(self, path: Path | None = None, parents: bool = False) -> None:
        """Creates an instance of TOMLStore.

        Args:
            path: Path to TOML file. Default location is the user data dir.
            parents: Whether to create parent directories, if they don't exist.
                Default is False.
        """
        self._file_path: Path = self._default_file_path
        if path:
            self._file_path = path

        self.path.parent.mkdir(parents=parents, exist_ok=True)

        self._pack: Pack = Pack()

        if not self.path.is_file():
            self._doc = tomlkit.document()
            with open(self.path, "w") as tf:
                tomlkit.dump(self._doc, tf)
            return

        with open(self.path, "r") as tf:
            self._doc = tomlkit.load(tf)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({Stringer.truncate(str(self.path), self._repr_max_path_len)})"

    @property
    def path(self) -> Path:
        return self._file_path

    @property
    def acronyms(self) -> Pack:
        return self._pack

    def add_acronym(self, acronym: Acronym) -> None:
        tab = tomlkit.table()
        tab.append("meaning", acronym.meaning)
        tab.append("description", acronym.description)
        tab.append("reference", acronym.reference)
        # TODO: Handle duplicate acronyms with alternate meanings.
        self._doc[acronym.name] = tab

    def load(self) -> None:
        """Loads acronyms in from the file store. Overwrites the current store."""
        self._pack = Pack()
        with open(self.path, "r") as tf:
            self._doc = tomlkit.load(tf)
        self._pack.add_many(self._doc)

    def write(self):
        with open(self.path, "w") as tf:
            tomlkit.dump(self._doc, tf)
