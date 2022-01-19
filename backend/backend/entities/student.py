from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.entities.types import ID, Gender, StudentYear, StudentSemester
from backend.entities.professor import Professor


class Student(BaseModel):
    id_: ID

    full_name: str
    admission_date: date

    email: Optional[str]
    gender: Optional[Gender]
    area_of_study: Optional[str]

    supervisor: Optional[Professor]
    advisor1: Optional[Professor]
    advisor2: Optional[Professor]

    @property
    def current_year(self) -> StudentYear:
        raise NotImplementedError()

    @property
    def current_semester(self) -> StudentSemester:
        raise NotImplementedError()

    class Config:
        orm_mode = True
