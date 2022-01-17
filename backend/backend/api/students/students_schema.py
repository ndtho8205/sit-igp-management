from typing import TYPE_CHECKING

from sqlalchemy import Date, Enum, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from backend.core import types
from backend.db.base_schema import BaseSchema


if TYPE_CHECKING:
    from backend.api.professors.professors_schema import ProfessorSchema


class StudentSchema(BaseSchema):
    __tablename__ = "students"

    full_name = Column(String(256), nullable=False)
    admission_date = Column(Date, index=True, nullable=False)

    email = Column(String(256), index=True, unique=True)
    gender = Column(Enum(types.Gender))
    area_of_study = Column(String(256))

    supervisor_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
    advisor1_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )
    advisor2_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
    )

    supervisor: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        backref="supervisees",
        foreign_keys=supervisor_id,
    )
    advisor1: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        backref="primary_advisees",
        foreign_keys=advisor1_id,
    )
    advisor2: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        backref="secondary_advisees",
        foreign_keys=advisor2_id,
    )
