from typing import Optional

from pydantic import BaseModel

from backend.core import types


class BasePresentationEvaluation(BaseModel):
    presentation_id: types.ID
    reviewer_id: types.ID

    score_research_goal: types.ScoreInt
    score_delivery: types.ScoreInt
    score_visual_aid: types.ScoreInt
    score_time: types.ScoreInt
    score_qa: types.ScoreInt


class PresentationEvaluation(BasePresentationEvaluation):
    id_: types.ID

    comment: Optional[str]

    is_deleted: bool

    class Config:
        orm_mode = True
