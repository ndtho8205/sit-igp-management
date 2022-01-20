from typing import Optional

from datetime import date

from sqlalchemy import Date, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from backend.entities.types import ID
from backend.adapters.pg.schemas.base import BaseSchema


class PresentationSchema(BaseSchema):
    __tablename__ = "presentations"

    student_id: ID = Column(
        UUID(as_uuid=True),
        ForeignKey("students.id_"),
        index=True,
        nullable=False,
    )
    presentation_date: date = Column(Date, index=True, nullable=False)

    presentation_length: Optional[str] = Column(String(256))

    session_chair_id: Optional[ID] = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
    reviewer1_id: Optional[ID] = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
    reviewer2_id: Optional[ID] = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
    reviewer3_id: Optional[ID] = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
    reviewer4_id: Optional[ID] = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
