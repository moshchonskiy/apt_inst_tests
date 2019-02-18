import pytest
from utils.shell_executor import ShellExecutor


@pytest.fixture(scope="class")
def shell_executor():
    return ShellExecutor()


@pytest.fixture()
def remove_rolldice(shell_executor):
    shell_executor.apt_purge_pkg('rolldice')
