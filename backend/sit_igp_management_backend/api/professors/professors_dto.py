from typing import Optional

from pydantic import EmailStr, BaseModel

from sit_igp_management_backend.core import types
from sit_igp_management_backend.api.professors.professors_entities import BaseProfessor


class ProfessorCreateDto(BaseProfessor):
    pass


class ProfessorUpdateDto(BaseModel):
    full_name: Optional[types.FullName]
    email: Optional[EmailStr]


class ProfessorResponseDto(BaseProfessor):
    id_: int
    is_active: bool

    class Config:
        orm_mode = True
