from click.testing import CliRunner, Result

from py_acronym_keeper import config
from py_acronym_keeper.cli.root import root_group
from py_acronym_keeper.printer import Printer
from py_acronym_keeper.toml_store import TOMLStore


def test_happy_path() -> None:
    runner = CliRunner()
    store: TOMLStore = TOMLStore(config.REPO_TEST_DATA_DIR / "happy_path.toml")
    result: Result = runner.invoke(
        root_group,
        ["list"],
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
    result: Result = runner.invoke(root_group, ["list"])
    assert result.output == "\n"


def test_max_line_length_validation() -> None:
    runner = CliRunner()

    result: Result = runner.invoke(root_group, ["list", "--max-length", "2"])
    assert result.exit_code != 0
    assert "Invalid value for '--max-length'" in result.output

    result = runner.invoke(root_group, ["list", "-m", "-1"])
    assert result.exit_code == 0

    result = runner.invoke(
        root_group, ["list", "-m", str(Printer._default_max_line_length + 5)]
    )
    assert result.exit_code == 0
