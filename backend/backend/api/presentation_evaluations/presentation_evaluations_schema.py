from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from backend.core import types
from backend.db.base_schema import BaseSchema


class PresentationEvaluationSchema(BaseSchema):
    __tablename__ = "presentation_evaluations"

    presentation_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("presentations.id_"),
        index=True,
        nullable=False,
    )
    reviewer_id: types.ID = Column(
        UUID(as_uuid=True),
        ForeignKey("professors.id_"),
        index=True,
        nullable=False,
    )

    score_research_goal = Column(Integer, nullable=False)
    score_delivery = Column(Integer, nullable=False)
    score_visual_aid = Column(Integer, nullable=False)
    score_time = Column(Integer, nullable=False)
    score_qa = Column(Integer, nullable=False)
    comment = Column(String)