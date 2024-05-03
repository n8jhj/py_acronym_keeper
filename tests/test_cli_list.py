from click.testing import CliRunner, Result

from py_acronym_keeper import config
from py_acronym_keeper.cli.root import list_command
from py_acronym_keeper.printer import Printer
from py_acronym_keeper.toml_store import TOMLStore


def test_happy_path() -> None:
    runner = CliRunner()
    store: TOMLStore = TOMLStore(config.REPO_TEST_DATA_DIR / "happy_path.toml")
    result: Result = runner.invoke(
        list_command,
        [],
        obj={"store": store},
    )
    # There is one final newline, resulting in a final empty string. Leave that
    # one off.
    lines: list[str] = result.output.splitlines()[:-1]

    assert len(lines) == len(store.acronyms)

    assert (
        lines[0]
        == f"PAK : Py Acronym Keeper : A really cool Python package for storing acronyms."
    )

    assert "TLA" in lines[1]

    assert "ABC" in lines[2]
    assert len(lines[2]) == Printer._default_max_line_length


def test_empty_file() -> None:
    runner = CliRunner()
    result: Result = runner.invoke(list_command)
    assert result.output == ""
