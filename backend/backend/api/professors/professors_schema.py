from sqlalchemy import Column, String, Boolean

from backend.db.base_schema import BaseSchema


class ProfessorSchema(BaseSchema):
    __tablename__ = "professors"

    full_name = Column(String(256), nullable=False)
    email = Column(String(256), index=True, nullable=False, unique=True)

    is_verified = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
