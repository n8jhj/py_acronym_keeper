from py_acronym_keeper import config
from py_acronym_keeper.toml_store import TOMLStore


# TODO: Implement a test that checks that the default TOML file has the correct
# contents.


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
