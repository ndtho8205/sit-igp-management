from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.entities.types import ID, Gender, LongStr, FullName, UniversityEmailStr


class ProfessorCreateInput(BaseModel):
    full_name: FullName
    email: UniversityEmailStr
    is_verified: bool = False
    is_superuser: bool = False


class ProfessorUpdateInput(BaseModel):
    full_name: Optional[FullName]
    email: Optional[UniversityEmailStr]
    is_verified: Optional[bool]
    is_superuser: Optional[bool]


class StudentCreateInput(BaseModel):
    full_name: FullName
    admission_date: date

    email: Optional[UniversityEmailStr]
    gender: Optional[Gender]
    area_of_study: Optional[LongStr]

    supervisor_id: Optional[ID]
    advisor1_id: Optional[ID]
    advisor2_id: Optional[ID]


class StudentUpdateInput(BaseModel):
    full_name: Optional[FullName]
    admission_date: Optional[date]

    email: Optional[UniversityEmailStr]
    gender: Optional[Gender]
    area_of_study: Optional[LongStr]

    supervisor_id: Optional[ID]
    advisor1_id: Optional[ID]
    advisor2_id: Optional[ID]
