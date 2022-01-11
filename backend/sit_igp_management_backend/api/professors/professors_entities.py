from pydantic import EmailStr, BaseModel

from sit_igp_management_backend.core import types


class _BaseProfessor(BaseModel):
    full_name: types.FullName
    email: EmailStr


class Professor(_BaseProfessor):
    professor_id: int
    is_active: bool = False
    is_superuser: bool = False

    class Config:
        orm_mode = True
