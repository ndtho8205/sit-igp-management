# pylint: disable=no-member
# pragma: no cover"
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool, engine_from_config

from backend.db import BaseSchema
from backend.api import import_all_schemas
from backend.configs import app_config


config = context.config
fileConfig(str(config.config_file_name))
HEROKU_DB_URL = "postgresql://talcmiclppniwj:895444aaffc84ab7f0cc9d39ee19d5deb693ffab6f2e18aca72954d0ca20b47d@ec2-3-227-15-75.compute-1.amazonaws.com:5432/d8muuksf5n29ja"
# config.set_main_option("sqlalchemy.url", str(app_config.DATABASE_URL))
config.set_main_option("sqlalchemy.url", HEROKU_DB_URL)

import_all_schemas()
target_metadata = BaseSchema.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
