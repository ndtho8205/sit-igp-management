from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.core import types
from backend.api.professors.professors_entities import Professor


class BaseStudent(BaseModel):
    full_name: types.FullName
    admission_date: date


class Student(BaseStudent):
    id_: int
    email: Optional[types.UniversityEmailStr]
    gender: Optional[types.Gender]
    area_of_study: Optional[types.ShortStr]

    supervisor_id: Optional[int]
    advisor1_id: Optional[int]
    advisor2_id: Optional[int]

    supervisor: Optional[Professor]
    advisor1: Optional[Professor]
    advisor2: Optional[Professor]

    is_deleted: bool

    class Config:
        orm_mode = True
