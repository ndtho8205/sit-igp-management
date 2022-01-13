from datetime import date

from pydantic import EmailStr, BaseModel, validator

from sit_igp_management_backend.core import types
from sit_igp_management_backend.core.validators import validate_university_email


class BaseStudent(BaseModel):
    full_name: types.FullName
    admission_date: date


class Student(BaseStudent):
    id_: int
    email: EmailStr
    gender: types.Gender
    area_of_study: types.ShortStr

    supervisor_id: int
    advisor1_id: int
    advisor2_id: int

    _check_university_email = validator("email", allow_reuse=True)(
        validate_university_email,
    )

    class Config:
        orm_mode = True
