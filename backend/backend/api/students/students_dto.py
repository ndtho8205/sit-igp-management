from typing import Optional

from datetime import date

from pydantic import EmailStr, BaseModel, validator

from backend.core import types
from backend.core.validators import validate_university_email
from backend.api.students.students_entities import Student, BaseStudent


class BaseStudentDto(BaseModel):
    email: Optional[EmailStr]
    gender: Optional[types.Gender]
    area_of_study: Optional[types.ShortStr]

    supervisor_id: Optional[int]
    advisor1_id: Optional[int]
    advisor2_id: Optional[int]

    _check_university_email = validator("email", allow_reuse=True)(
        validate_university_email,
    )


class StudentCreateDto(BaseStudent, BaseStudentDto):
    pass


class StudentUpdateDto(BaseStudentDto):
    full_name: Optional[types.FullName]
    admission_date: Optional[date]


class StudentResponseDto(Student):
    pass
