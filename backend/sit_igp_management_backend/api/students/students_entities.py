from datetime import date

from pydantic import EmailStr, BaseModel

from sit_igp_management_backend.core import types


class _BaseStudent(BaseModel):
    full_name: types.FullName
    admission_date: date


class Student(_BaseStudent):
    student_id: int
    email: EmailStr
    gender: types.Gender
    area_of_study: types.ShortStr

    supervisor_id: int
    advisor1_id: int
    advisor2_id: int

    class Config:
        orm_mode = True
