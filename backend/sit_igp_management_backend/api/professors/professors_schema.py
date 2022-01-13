from typing import TYPE_CHECKING, List

from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from sit_igp_management_backend.db.base_schema import BaseSchema


if TYPE_CHECKING:
    from sit_igp_management_backend.api.students import StudentSchema
    from sit_igp_management_backend.api.semester_end_presentations import (
        SemesterEndPresentationsSchema,
    )


class ProfessorSchema(BaseSchema):
    __tablename__ = "professors"

    full_name = Column(String(256), nullable=False)
    email = Column(String(256), index=True, nullable=False, unique=True)
    is_active = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    supervisees: List["StudentSchema"] = relationship(
        "StudentSchema",
        back_populates="supervisor",
        foreign_keys="StudentSchema.supervisor_id",
    )
    primary_advisees: List["StudentSchema"] = relationship(
        "StudentSchema",
        back_populates="advisor1",
        foreign_keys="StudentSchema.advisor1_id",
    )
    secondary_advisees: List["StudentSchema"] = relationship(
        "StudentSchema",
        back_populates="advisor2",
        foreign_keys="StudentSchema.advisor2_id",
    )
