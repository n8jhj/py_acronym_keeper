import pytest

from py_acronym_keeper import config
from py_acronym_keeper.toml_store import TOMLStore


def test_default_contents():
    store = TOMLStore()
    store.load()
    acronyms = store.acronyms

    assert len(acronyms) == 0
    assert bool(acronyms) == False
    assert "hello" not in acronyms
    with pytest.raises(KeyError):
        acronyms["anything"]


def test_load():
    store = TOMLStore(config.REPO_TEST_DATA_DIR / "happy_path.toml")
    store.load()
    acronyms = store.acronyms

    assert "PAK" in acronyms
    pak = acronyms["PAK"]
    assert pak.name == "PAK"
    assert pak.meaning == "Py Acronym Keeper"
    assert pak.description == "A really cool Python package for storing acronyms."
    assert pak.reference == "https://github.com/n8jhj/py_acronym_keeper"

    assert "TLA" in acronyms
    tla = acronyms["TLA"]
    assert tla.reference == ""
