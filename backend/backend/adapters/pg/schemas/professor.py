from sqlalchemy import Column, String, Boolean

from backend.adapters.pg.schemas.base import BaseSchema


class ProfessorSchema(BaseSchema):
    __tablename__ = "professors"

    full_name: str = Column(String(256), nullable=False)
    email: str = Column(String(256), index=True, nullable=False, unique=True)

    is_verified: bool = Column(Boolean, default=False, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
