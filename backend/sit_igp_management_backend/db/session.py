from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sit_igp_management_backend.core.config import config


engine = create_engine(
    str(config.SQLALCHEMY_DATABASE_URI),
    pool_pre_ping=True,
)

DbSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
