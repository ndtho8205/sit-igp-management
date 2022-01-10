from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declarative_base


class _Base:
    # pylint: disable=invalid-name
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False,
        onupdate=func.now(),
    )


BaseSchema = declarative_base(cls=_Base)
