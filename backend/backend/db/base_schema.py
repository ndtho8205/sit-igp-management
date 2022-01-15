from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import declarative_base


class _Base:
    # pylint: disable=invalid-name
    id_ = Column(Integer, index=True, nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime,
        nullable=False,
        onupdate=func.now(),
        server_default=func.now(),
    )


BaseSchema = declarative_base(cls=_Base)
