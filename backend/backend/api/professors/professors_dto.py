from typing import Optional

from pydantic import BaseModel

from backend.core import types
from backend.api.professors.professors_entities import Professor, BaseProfessor


class ProfessorCreateDto(BaseProfessor):
    pass


class ProfessorUpdateDto(BaseModel):
    full_name: Optional[types.FullName]
    email: Optional[types.UniversityEmailStr]
    is_deleted: Optional[bool]
    is_verified: Optional[bool]


class ProfessorResponseDto(Professor):
    pass
