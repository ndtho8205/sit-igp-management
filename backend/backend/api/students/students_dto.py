from typing import Any, Optional

from datetime import date

from pydantic import BaseModel, validator
from sqlalchemy.orm.query import Query

from backend.core import types
from backend.api.students.students_entities import Student, BaseStudent
from backend.api.professors.professors_entities import BaseProfessor


class BaseStudentDto(BaseModel):
    email: Optional[types.UniversityEmailStr]
    gender: Optional[types.Gender]
    area_of_study: Optional[types.ShortStr]

    supervisor_id: Optional[types.ID]
    advisor1_id: Optional[types.ID]
    advisor2_id: Optional[types.ID]


class StudentCreateDto(BaseStudent, BaseStudentDto):
    pass


class StudentUpdateDto(BaseStudentDto):
    is_deleted: Optional[bool]

    full_name: Optional[types.FullName]
    admission_date: Optional[date]


class StudentResponseDto(Student):
    supervisor: Optional[BaseProfessor]
    advisor1: Optional[BaseProfessor]
    advisor2: Optional[BaseProfessor]

    # pylint: disable=invalid-name,no-self-argument,no-self-use
    @validator("supervisor", "advisor1", "advisor2", pre=True)
    def evaluate_lazy_columns(cls, v: Any) -> Any:  # noqa: B902, N805
        if isinstance(v, Query):
            return v.all()
        return v
