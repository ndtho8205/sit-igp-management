import uuid

from sqlalchemy import Column, Boolean, DateTime, func
from sqlalchemy.orm import as_declarative
from sqlalchemy.dialects.postgresql import UUID

from backend.entities.types import ID


@as_declarative()
class BaseSchema:
    # pylint: disable=invalid-name
    id_: ID = Column(
        UUID(as_uuid=True),
        index=True,
        nullable=False,
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
    )

    is_deleted = Column(Boolean, default=False, index=True, nullable=False)

    created_at = Column(DateTime, default=func.now(), index=True, nullable=False)
    updated_at = Column(
        DateTime,
        nullable=False,
        onupdate=func.now(),
        server_default=func.now(),
    )
