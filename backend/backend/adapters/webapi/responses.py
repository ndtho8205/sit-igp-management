from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.entities.types import ID, Gender, LongStr, FullName, UniversityEmailStr
from backend.entities.professor import Professor


class _StudentSupervisor(BaseModel):
    id_: ID
    full_name: str
    email: str


class ProfessorResponse(Professor):
    pass


class StudentResponse(BaseModel):
    id_: ID
    full_name: FullName
    admission_date: date

    email: Optional[UniversityEmailStr]
    gender: Optional[Gender]
    area_of_study: Optional[LongStr]

    supervisor: Optional[_StudentSupervisor]
    advisor1: Optional[_StudentSupervisor]
    advisor2: Optional[_StudentSupervisor]
