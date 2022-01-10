from sqlalchemy import Date, Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from sit_igp_management_backend.db.session import Base


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    gender = Column(String)
    area_of_study = Column(String)
    admission_date = Column(Date)

    supervisor_id = Column(Integer, ForeignKey("professors.professor_id"))
    supervisor = relationship("Professor", back_populates="students")

    advisor1_id = Column(Integer, ForeignKey("professors.advisor1_id"))
    supervisor = relationship("Professor", back_populates="students")

    advisor2_id = Column(Integer, ForeignKey("professors.advisor2_id"))
