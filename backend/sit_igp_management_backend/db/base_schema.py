from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declarative_base


_Base = declarative_base()


class BaseSchema(_Base):
    # pylint: disable=invalid-name
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False,
        onupdate=func.now(),
    )
