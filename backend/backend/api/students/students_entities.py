from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.core import types


class BaseStudent(BaseModel):
    full_name: types.FullName
    admission_date: date


class Student(BaseStudent):
    id_: types.ID
    email: Optional[types.UniversityEmailStr]
    gender: Optional[types.Gender]
    area_of_study: Optional[types.ShortStr]

    supervisor_id: Optional[types.ID]
    advisor1_id: Optional[types.ID]
    advisor2_id: Optional[types.ID]

    is_deleted: bool

    class Config:
        orm_mode = True
