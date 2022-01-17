from sqlalchemy import Date, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from backend.core import types
from backend.db.base_schema import BaseSchema


class PresentationSchema(BaseSchema):
    __tablename__ = "presentations"

    student_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("students.id_"),
        index=True,
        nullable=False,
    )
    presentation_date = Column(Date, index=True, nullable=False)
    presentation_length = Column(String)

    reviewer1_id: types.ID = Column(UUID(as_uuid=True), ForeignKey("professors.id_"))
    reviewer2_id: types.ID = Column(UUID(as_uuid=True), ForeignKey("professors.id_"))
    reviewer3_id: types.ID = Column(UUID(as_uuid=True), ForeignKey("professors.id_"))
    reviewer4_id: types.ID = Column(UUID(as_uuid=True), ForeignKey("professors.id_"))
    reviewer5_id: types.ID = Column(UUID(as_uuid=True), ForeignKey("professors.id_"))
