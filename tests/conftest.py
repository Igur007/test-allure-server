import pytest

from harness.config.configuration import Config


@pytest.fixture(scope="session", autouse=True)
def config() -> Config:
    return Config()
