from uuid import uuid4
from pathlib import Path

import pytest

import alembic
from alembic.config import Config

from fastapi.testclient import TestClient

from backend.configs import app_config
from backend.init_app import init_app


@pytest.fixture(scope="session")
def _apply_migrations():  # type: ignore
    alembic_config = Config(str(Path(__file__).parents[1] / "alembic.ini"))
    alembic.command.upgrade(alembic_config, "head")
    yield
    alembic.command.downgrade(alembic_config, "base")


@pytest.fixture()
def client(_apply_migrations: None) -> TestClient:
    return TestClient(init_app(app_config))


@pytest.fixture()
def random_id() -> str:
    return str(uuid4())
