from typing import TYPE_CHECKING

from sqlalchemy import Date, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from sit_igp_management_backend.db.base_schema import BaseSchema


if TYPE_CHECKING:
    from sit_igp_management_backend.api.students import StudentSchema


class SemesterEndPresentationsSchema(BaseSchema):
    __tablename__ = "semester_end_presentations"

    student_id = Column(Integer, ForeignKey("students.id_"), nullable=False)
    presentation_date = Column(Date, index=True, nullable=False)
    presentation_length = Column(String)

    reviewer1_id = Column(Integer, ForeignKey("professors.id_"), nullable=False)
    reviewer2_id = Column(Integer, ForeignKey("professors.id_"), nullable=False)
    reviewer3_id = Column(Integer, ForeignKey("professors.id_"), nullable=False)
    reviewer4_id = Column(Integer, ForeignKey("professors.id_"), nullable=False)

    student: "StudentSchema" = relationship(
        "StudentSchema",
        back_populates="semester_end_presentations",
    )
