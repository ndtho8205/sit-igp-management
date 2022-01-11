from typing import Optional

from pydantic import EmailStr, BaseModel

from sit_igp_management_backend.core import types

from .professors_entities import ProfessorBase


class CreateProfessorDto(ProfessorBase):
    pass


class UpdateProfessorDto(BaseModel):
    full_name: Optional[types.FullName]
    email: Optional[EmailStr]
    is_active: Optional[bool]
