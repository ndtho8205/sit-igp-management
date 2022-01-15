from sqlalchemy import Date, Column, String, Integer, ForeignKey

from backend.db.base_schema import BaseSchema


class PresentationSchema(BaseSchema):
    __tablename__ = "presentations"

    student_id = Column(Integer, ForeignKey("students.id_"), index=True, nullable=False)
    presentation_date = Column(Date, index=True, nullable=False)
    presentation_length = Column(String)

    reviewer1_id = Column(Integer, ForeignKey("professors.id_"))
    reviewer2_id = Column(Integer, ForeignKey("professors.id_"))
    reviewer3_id = Column(Integer, ForeignKey("professors.id_"))
    reviewer4_id = Column(Integer, ForeignKey("professors.id_"))
    reviewer5_id = Column(Integer, ForeignKey("professors.id_"))
