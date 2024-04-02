"""Defines the Acronym class."""


class Acronym:
    def __init__(
        self, name: str, meaning: str, description: str, reference: str
    ) -> None:
        # This is the actual acronym, e.g. TLA.
        self.name: str = name
        self.meaning: str = meaning
        self.description: str = description
        self.reference: str = reference
