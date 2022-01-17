from pydantic import BaseModel

from backend.core import types


class BaseProfessor(BaseModel):
    full_name: types.FullName
    email: types.UniversityEmailStr

    class Config:
        orm_mode = True


class Professor(BaseProfessor):
    id_: types.ID
    is_deleted: bool

    is_verified: bool
    is_superuser: bool
