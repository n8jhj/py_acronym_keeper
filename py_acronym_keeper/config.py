"""App-wide configuration."""

from pathlib import Path

from platformdirs import user_data_path


REPO_ROOT_DIR: Path = Path(__file__).parents[1]
REPO_TEST_DIR: Path = REPO_ROOT_DIR / "tests"
REPO_TEST_DATA_DIR: Path = REPO_TEST_DIR / "data"
REPR_MAX_PATH_LEN: int = 30
USER_DATA_DIR: Path = user_data_path("py_acronym_keeper", "n8jhj")


# Dynamically determined Paths for easy monkeypatching in tests.


def user_default_config_path() -> Path:
    return USER_DATA_DIR / "config.toml"


def user_default_store_path() -> Path:
    return USER_DATA_DIR / "store.toml"
