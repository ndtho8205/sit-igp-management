from typing import TYPE_CHECKING

from sqlalchemy import Date, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from backend.core import types
from backend.db.base_schema import BaseSchema


if TYPE_CHECKING:
    from backend.api.students.students_schema import StudentSchema
    from backend.api.professors.professors_schema import ProfessorSchema


class PresentationSchema(BaseSchema):
    __tablename__ = "presentations"

    student_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("students.id_"),
        index=True,
        nullable=False,
    )
    presentation_date = Column(Date, index=True, nullable=False)

    presentation_length = Column(String(256))

    reviewer1_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
    reviewer2_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
    reviewer3_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
    reviewer4_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
    reviewer5_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )

    student: "StudentSchema" = relationship(
        "StudentSchema",
        backref="presentations",
        foreign_keys=student_id,
    )
    reviewer1: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        backref="presentations_1",
        foreign_keys=reviewer1_id,
    )
    reviewer2: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        backref="presentations_2",
        foreign_keys=reviewer2_id,
    )
    reviewer3: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        backref="presentations_3",
        foreign_keys=reviewer3_id,
    )
    reviewer4: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        backref="presentations_4",
        foreign_keys=reviewer4_id,
    )
    reviewer5: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        backref="presentations_5",
        foreign_keys=reviewer5_id,
    )
