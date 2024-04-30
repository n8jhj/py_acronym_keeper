"""Pytest configuration. Ref.
https://docs.pytest.org/en/7.1.x/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files
"""

from pathlib import Path
import shutil

from py_acronym_keeper import config

# Patch the user data directory to point to a test location instead of the real
# one.
config.USER_DATA_DIR = config.REPO_TEST_DIR / "temp"
config.USER_DATA_DIR.mkdir(exist_ok=True)


def pytest_sessionstart(session):
    """Called after the Session object has been created and before performing
    collection and entering the run test loop.
    """
    # Make sure you don't delete the user data dir on your actual system!
    to_rm: Path = config.USER_DATA_DIR
    if (
        not config.REPO_TEST_DIR.expanduser().absolute()
        in to_rm.expanduser().absolute().parents
    ):
        raise RuntimeError(f"Dangerous! You were about to delete: {to_rm}")
    shutil.rmtree(to_rm)
