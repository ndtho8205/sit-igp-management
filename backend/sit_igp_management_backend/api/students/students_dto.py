from typing import Optional

from datetime import date

from pydantic import EmailStr, BaseModel

from sit_igp_management_backend.core import types

from .students_entities import _BaseStudent


class _BaseStudentDto(BaseModel):
    email: Optional[EmailStr] = None
    gender: Optional[types.Gender] = None
    area_of_study: Optional[types.ShortStr] = None

    supervisor_id: Optional[int] = None
    advisor1_id: Optional[int] = None
    advisor2_id: Optional[int] = None


class CreateStudentDto(_BaseStudentDto, _BaseStudent):
    pass


class UpdateStudentDto(_BaseStudentDto):
    full_name: Optional[types.FullName] = None
    admission_date: Optional[date] = None
