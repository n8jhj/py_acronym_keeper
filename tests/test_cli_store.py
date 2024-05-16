from click.testing import CliRunner, Result

from py_acronym_keeper import config
from py_acronym_keeper.cli.root import root_group
from py_acronym_keeper.toml_store import TOMLStore


def test_happy_path() -> None:
    runner = CliRunner()
    store: TOMLStore = TOMLStore(config.REPO_TEST_DATA_DIR / "happy_path.toml")
    result: Result = runner.invoke(
        root_group,
        ["store"],
        obj={"store": store},
    )

    assert result.output.strip() == str(store.path)
