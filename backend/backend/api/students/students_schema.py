from sqlalchemy import Date, Enum, Column, String, Integer, ForeignKey

from backend.core import types
from backend.db.base_schema import BaseSchema


class StudentSchema(BaseSchema):
    __tablename__ = "students"

    full_name = Column(String(256), nullable=False)
    email = Column(String(256), unique=True)
    gender = Column(Enum(types.Gender))
    area_of_study = Column(String(256))
    admission_date = Column(Date, index=True, nullable=False)

    supervisor_id = Column(Integer, ForeignKey("professors.id_"))
    advisor1_id = Column(Integer, ForeignKey("professors.id_"))
    advisor2_id = Column(Integer, ForeignKey("professors.id_"))
