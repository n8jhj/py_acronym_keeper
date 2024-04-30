"""App-wide configuration."""

from pathlib import Path

from platformdirs import user_data_path


REPO_ROOT_DIR: Path = Path(__file__).parents[1]
REPO_TEST_DIR: Path = REPO_ROOT_DIR / "tests"
USER_DATA_DIR: Path = user_data_path("py_acronym_keeper", "n8jhj")
