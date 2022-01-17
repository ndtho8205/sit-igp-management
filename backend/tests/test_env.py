import os


def test_env() -> None:
    assert os.environ["APP_ENV"] == "test"
