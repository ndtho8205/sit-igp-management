from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Float
from sqlalchemy.dialects.postgresql import UUID

from backend.entities.types import ID, Score
from backend.adapters.pg.schemas.base import BaseSchema


class LabSeminarEvaluationSchema(BaseSchema):
    __tablename__ = "lab_seminar_evaluations"

    presentation_id: ID = Column(
        UUID(as_uuid=True),
        ForeignKey("presentations.id_"),
        index=True,
        nullable=False,
    )
    score_daily_activities_1: Score = Column(Float, nullable=False)
    score_daily_activities_2: Score = Column(Float, nullable=False)
    score_meeting_presentation_1: Score = Column(Float, nullable=False)
    score_meeting_presentation_2: Score = Column(Float, nullable=False)

    course_score: Score = Column(Float, nullable=False)
