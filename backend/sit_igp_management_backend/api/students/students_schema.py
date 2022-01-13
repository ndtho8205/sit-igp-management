from typing import TYPE_CHECKING, List

from sqlalchemy import Date, Enum, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from sit_igp_management_backend.core import types
from sit_igp_management_backend.db.base_schema import BaseSchema


if TYPE_CHECKING:
    from sit_igp_management_backend.api.professors import ProfessorSchema
    from sit_igp_management_backend.api.semester_end_presentations import (
        SemesterEndPresentationsSchema,
    )


class StudentSchema(BaseSchema):
    __tablename__ = "students"

    full_name = Column(String(256), nullable=False)
    email = Column(String(256), unique=True)
    gender = Column(Enum(types.Gender))
    area_of_study = Column(String(256))
    admission_date = Column(Date, index=True, nullable=False)

    supervisor_id = Column(Integer, ForeignKey("professors.id_"))
    advisor1_id = Column(Integer, ForeignKey("professors.id_"))
    advisor2_id = Column(Integer, ForeignKey("professors.id_"))

    supervisor: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        back_populates="supervisees",
        foreign_keys=[supervisor_id],
    )
    advisor1: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        back_populates="primary_advisees",
        foreign_keys=[advisor1_id],
    )
    advisor2: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        back_populates="secondary_advisees",
        foreign_keys=[advisor2_id],
    )

    semester_end_presentations: List["SemesterEndPresentationsSchema"] = relationship(
        "SemesterEndPresentationsSchema",
        back_populates="student",
    )
