from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from backend.core import types
from backend.db.base_schema import BaseSchema


if TYPE_CHECKING:
    from backend.api.professors.professors_schema import ProfessorSchema
    from backend.api.presentations.presentations_schema import PresentationSchema


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

    comment = Column(String(256))

    presentation: "PresentationSchema" = relationship(
        "PresentationSchema",
        backref="evaluations",
        foreign_keys=presentation_id,
    )
    reviewer: "ProfessorSchema" = relationship(
        "ProfessorSchema",
        backref="evaluations",
        foreign_keys=reviewer_id,
    )
