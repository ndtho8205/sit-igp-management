from typing import Any, Optional

from datetime import date

from pydantic import BaseModel, validator
from sqlalchemy.orm.query import Query

from backend.core import types
from backend.api.students.students_entities import Student, BaseStudent
from backend.api.professors.professors_entities import BaseProfessor
from backend.api.presentations.presentations_entities import (
    Presentation,
    BasePresentation,
)


class BasePresentationDto(BaseModel):
    presentation_length: Optional[str]

    reviewer1_id: Optional[types.ID]
    reviewer2_id: Optional[types.ID]
    reviewer3_id: Optional[types.ID]
    reviewer4_id: Optional[types.ID]
    reviewer5_id: Optional[types.ID]


class PresentationCreateDto(BasePresentation, BasePresentationDto):
    pass


class PresentationUpdateDto(BasePresentationDto):
    is_deleted: Optional[bool]

    student_id: Optional[types.ID]
    presentation_date: Optional[date]


class PresentationResponseDto(Presentation):
    student: Optional[BaseStudent]
    reviewer1: Optional[BaseProfessor]
    reviewer2: Optional[BaseProfessor]
    reviewer3: Optional[BaseProfessor]
    reviewer4: Optional[BaseProfessor]
    reviewer5: Optional[BaseProfessor]

    # pylint: disable=invalid-name,no-self-argument,no-self-use
    @validator(
        "student",
        "reviewer1",
        "reviewer2",
        "reviewer3",
        "reviewer4",
        "reviewer5",
        pre=True,
    )
    def evaluate_lazy_columns(cls, v: Any) -> Any:  # noqa: B902, N805
        if isinstance(v, Query):
            return v.all()
        return v
