from typing import Iterator

from sqlalchemy.orm import Session

from sit_igp_management_backend.db.session import DbSession


def get_db() -> Iterator[Session]:
    db_session = DbSession()
    try:
        yield db_session
    finally:
        db_session.close()
