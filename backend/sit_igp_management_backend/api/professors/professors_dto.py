from typing import Optional

from pydantic import EmailStr, BaseModel

from sit_igp_management_backend.core import types

from .professors_entities import _BaseProfessor


class CreateProfessorDto(_BaseProfessor):
    pass


class UpdateProfessorDto(BaseModel):
    full_name: Optional[types.FullName] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
