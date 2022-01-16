from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.core import types
from backend.api.students.students_entities import Student, BaseStudent


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
    pass
