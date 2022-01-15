from pydantic import BaseModel

from backend.core import types


class BaseProfessor(BaseModel):
    full_name: types.FullName
    email: types.UniversityEmailStr


class Professor(BaseProfessor):
    id_: int
    is_verified: bool
    is_superuser: bool
    is_deleted: bool

    class Config:
        orm_mode = True
