from typing import Optional

from datetime import date

from sqlalchemy import Date, Enum, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from backend.entities.types import Gender
from backend.adapters.pg.schemas.base import BaseSchema


class StudentSchema(BaseSchema):
    __tablename__ = "students"

    full_name: str = Column(String(256), nullable=False)
    admission_date: date = Column(Date, index=True, nullable=False)

    email: Optional[str] = Column(String(256), index=True, unique=True)
    gender: Optional[Gender] = Column(Enum(Gender))
    area_of_study: Optional[str] = Column(String(2048))

    supervisor_id: Optional[str] = Column(UUID, ForeignKey("professors.id_"), index=True)
    advisor1_id: Optional[str] = Column(UUID, ForeignKey("professors.id_"), index=True)
    advisor2_id: Optional[str] = Column(UUID, ForeignKey("professors.id_"), index=True)
