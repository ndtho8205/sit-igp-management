from typing import Optional

from sqlalchemy import Float, Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from backend.entities.types import ID
from backend.adapters.pg.schemas.base import BaseSchema


class PresentationEvaluationSchema(BaseSchema):
    __tablename__ = "presentation_evaluations"

    presentation_id: ID = Column(
        UUID(as_uuid=True),
        ForeignKey("presentations.id_"),
        index=True,
        nullable=False,
    )
    reviewer_id: ID = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
        nullable=False,
    )
    score_research_goal: int = Column(Integer, nullable=False)
    score_delivery: int = Column(Integer, nullable=False)
    score_visual_aid: int = Column(Integer, nullable=False)
    score_time: int = Column(Integer, nullable=False)
    score_qa: int = Column(Integer, nullable=False)

    question_score: float = Column(Float, nullable=False)

    comment: Optional[str] = Column(String(256))
