from sqlalchemy import Column, Boolean, Integer, DateTime, func
from sqlalchemy.orm import as_declarative


@as_declarative()
class BaseSchema:
    # pylint: disable=invalid-name
    id_ = Column(Integer, index=True, nullable=False, primary_key=True, unique=True)
    is_deleted = Column(Boolean, default=False, index=True, nullable=False)
    created_at = Column(DateTime, default=func.now(), index=True, nullable=False)
    updated_at = Column(
        DateTime,
        nullable=False,
        onupdate=func.now(),
        server_default=func.now(),
    )
