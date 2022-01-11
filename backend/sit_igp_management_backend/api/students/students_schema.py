from sqlalchemy import Date, Enum, Column, String, Integer, ForeignKey

from sit_igp_management_backend.core import types
from sit_igp_management_backend.db.base_schema import BaseSchema


class StudentSchema(BaseSchema):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True, nullable=False)
    full_name = Column(String(256), nullable=False)
    email = Column(String(256), unique=True, index=True)
    gender = Column(Enum(types.Gender))
    area_of_study = Column(String(256))
    admission_date = Column(Date, index=True, nullable=False)

    supervisor_id = Column(Integer, ForeignKey("professors.professor_id"))
    advisor1_id = Column(Integer, ForeignKey("professors.professor_id"))
    advisor2_id = Column(Integer, ForeignKey("professors.professor_id"))
