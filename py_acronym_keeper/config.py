"""App-wide configuration."""

from pathlib import Path

from platformdirs import user_data_path


REPO_ROOT_DIR: Path = Path(__file__).parents[1]
REPO_TEST_DIR: Path = REPO_ROOT_DIR / "tests"
REPO_TEST_DATA_DIR: Path = REPO_TEST_DIR / "data"
USER_DATA_DIR: Path = user_data_path("py_acronym_keeper", "n8jhj")
USER_DEFAULT_STORE_PATH: Path = USER_DATA_DIR / "store.toml"
