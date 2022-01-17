from typing import Optional

from pydantic import BaseModel

from backend.core import types
from backend.api.presentation_evaluations.presentation_evaluations_entities import (
    PresentationEvaluation,
    BasePresentationEvaluation,
)


class BasePresentationEvaluationDto(BasePresentationEvaluation):
    pass


class PresentationEvaluationCreateDto(BasePresentationEvaluationDto):
    comment: Optional[str]


class PresentationEvaluationUpdateDto(BaseModel):
    score_research_goal: Optional[types.ScoreInt]
    score_delivery: Optional[types.ScoreInt]
    score_visual_aid: Optional[types.ScoreInt]
    score_time: Optional[types.ScoreInt]
    score_qa: Optional[types.ScoreInt]
    comment: Optional[str]

    is_deleted: Optional[bool]


class PresentationEvaluationResponseDto(PresentationEvaluation):
    pass
