"""Handles TOML file storage."""

from pathlib import Path

import tomlkit

from . import config
from .acronym import Acronym


class TOMLStore:
    """Describes the TOML structure used for storing acronyms."""

    _file_path: Path = config.USER_DATA_DIR / "acronyms.toml"

    def __init__(self) -> None:
        self._file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self._file_path.is_file():
            self.doc = tomlkit.document()
            self.doc["acronym"] = tomlkit.table()
            with open(self._file_path, "w") as tf:
                tomlkit.dump(self.doc, tf)
            return

        with open(self._file_path, "r") as tf:
            self.doc = tomlkit.load(tf)

    def add_acronym(self, acronym: Acronym) -> None:
        tab = tomlkit.table()
        tab.append("meaning", acronym.meaning)
        tab.append("description", acronym.description)
        tab.append("reference", acronym.reference)
        self.doc["acronym"][acronym.name] = tab

    def write(self):
        with open(self._file_path, "w") as tf:
            tomlkit.dump(self.doc, tf)
