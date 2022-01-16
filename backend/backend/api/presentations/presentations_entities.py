from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.core import types


class BasePresentation(BaseModel):
    student_id: types.ID
    presentation_date: date


class Presentation(BasePresentation):
    id_: types.ID
    presentation_length: Optional[str]

    reviewer1_id: Optional[types.ID]
    reviewer2_id: Optional[types.ID]
    reviewer3_id: Optional[types.ID]
    reviewer4_id: Optional[types.ID]
    reviewer5_id: Optional[types.ID]

    is_deleted: bool

    class Config:
        orm_mode = True
