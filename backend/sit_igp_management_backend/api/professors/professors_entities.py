from pydantic import EmailStr, BaseModel, validator

from sit_igp_management_backend.core import types
from sit_igp_management_backend.core.validators import validate_university_email


class BaseProfessor(BaseModel):
    full_name: types.FullName
    email: EmailStr

    _check_university_email = validator("email", allow_reuse=True)(
        validate_university_email,
    )


class Professor(BaseProfessor):
    id_: int
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True
