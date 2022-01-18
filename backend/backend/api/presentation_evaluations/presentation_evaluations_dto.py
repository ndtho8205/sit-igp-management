from typing import Any, Optional

from pydantic import BaseModel, validator
from sqlalchemy.orm.query import Query

from backend.core import types
from backend.api.professors.professors_entities import BaseProfessor
from backend.api.presentations.presentations_entities import Presentation
from backend.api.presentation_evaluations.presentation_evaluations_entities import (
    PresentationEvaluation,
    BasePresentationEvaluation,
)


class PresentationEvaluationCreateDto(BasePresentationEvaluation):
    comment: Optional[types.ShortStr]


class PresentationEvaluationUpdateDto(BaseModel):
    is_deleted: Optional[bool]

    score_research_goal: Optional[types.ScoreInt]
    score_delivery: Optional[types.ScoreInt]
    score_visual_aid: Optional[types.ScoreInt]
    score_time: Optional[types.ScoreInt]
    score_qa: Optional[types.ScoreInt]

    comment: Optional[types.ShortStr]


class PresentationEvaluationResponseDto(PresentationEvaluation):
    presentation: Optional[Presentation]
    reviewer: Optional[BaseProfessor]

    # pylint: disable=invalid-name,no-self-argument,no-self-use
    @validator("presentation", "reviewer", pre=True)
    def evaluate_lazy_columns(cls, v: Any) -> Any:  # noqa: B902, N805
        if isinstance(v, Query):
            return v.all()
        return v
