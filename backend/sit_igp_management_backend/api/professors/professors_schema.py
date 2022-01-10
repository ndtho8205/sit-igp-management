from sqlalchemy import Column, String, Boolean, Integer

from sit_igp_management_backend.db.base_schema import BaseSchema


class ProfessorSchema(BaseSchema):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True, index=True, nullable=False)
    full_name = Column(String(256), nullable=False)
    email = Column(String(256), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
