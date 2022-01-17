from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.configs import app_config


engine = create_engine(
    str(app_config.DATABASE_URL),
    pool_pre_ping=True,
    future=True,
)

DbSession = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
