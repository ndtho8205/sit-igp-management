from pydantic import BaseModel

from backend.entities.types import ID


class Professor(BaseModel):
    id_: ID
    is_deleted: bool

    full_name: str
    email: str
    is_verified: bool
    is_superuser: bool

    class Config:
        orm_mode = True
