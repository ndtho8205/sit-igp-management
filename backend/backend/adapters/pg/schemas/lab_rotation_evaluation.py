from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Float
from sqlalchemy.dialects.postgresql import UUID

from backend.entities.types import ID, Score
from backend.adapters.pg.schemas.base import BaseSchema


class LabRotationEvaluationSchema(BaseSchema):
    __tablename__ = "lab_rotation_evaluations"

    presentation_id: ID = Column(
        UUID(as_uuid=True),
        ForeignKey("presentations.id_"),
        index=True,
        nullable=False,
    )

    course_score: Score = Column(Float, nullable=False)
