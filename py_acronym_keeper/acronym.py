"""Defines the Acronym and Pack classes."""

from collections.abc import Iterator, Mapping


class Acronym:
    """A single acronym."""

    def __init__(
        self, name: str, meaning: str, description: str, reference: str
    ) -> None:
        # This is the actual acronym, e.g. TLA.
        self.name: str = name
        self.meaning: str = meaning
        self.description: str = description
        self.reference: str = reference

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name})"

    @staticmethod
    def from_dict(name: str, fields: dict[str, str]) -> "Acronym":
        return Acronym(
            name, fields["meaning"], fields["description"], fields["reference"]
        )


class Pack(Mapping):
    """A collection of acronyms."""

    def __init__(self) -> None:
        self._acronyms: dict[str, Acronym] = {}

    def __repr__(self) -> str:
        return f"Pack({len(self)})"

    def __contains__(self, key: str) -> bool:
        return key in self._acronyms

    def __iter__(self) -> Iterator:
        return iter(self._acronyms.values())

    def __len__(self) -> int:
        return len(self._acronyms)

    def __getitem__(self, key: str) -> Acronym:
        return self._acronyms[key]

    def add(self, acronym: Acronym) -> None:
        """Adds a single acronym."""
        self._acronyms[acronym.name] = acronym

    def add_many(self, acronyms: Mapping[str, dict[str, str]]) -> None:
        """Adds a collection of acronyms."""
        for k, v in acronyms.items():
            self._acronyms[k] = Acronym.from_dict(k, v)
