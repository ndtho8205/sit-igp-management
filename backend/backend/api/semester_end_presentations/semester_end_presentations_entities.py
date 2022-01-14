from typing import Optional

from datetime import date

from pydantic import BaseModel


class BaseSemesterEndPresentation(BaseModel):
    student_id: int
    presentation_date: date


class SemesterEndPresentation(BaseSemesterEndPresentation):
    id_: int
    presentation_length: Optional[str]

    reviewer1_id: int
    reviewer2_id: int
    reviewer3_id: int
    reviewer4_id: int

    class Config:
        orm_mode = True
