from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.api.professors.professors_entities import Professor


class BasePresentation(BaseModel):
    student_id: int
    presentation_date: date


class Presentation(BasePresentation):
    id_: int
    presentation_length: Optional[str]

    reviewer1_id: Optional[int]
    reviewer2_id: Optional[int]
    reviewer3_id: Optional[int]
    reviewer4_id: Optional[int]
    reviewer5_id: Optional[int]

    reviewer1: Optional[Professor]
    reviewer2: Optional[Professor]
    reviewer3: Optional[Professor]
    reviewer4: Optional[Professor]
    reviewer5: Optional[Professor]

    is_deleted: bool

    class Config:
        orm_mode = True
