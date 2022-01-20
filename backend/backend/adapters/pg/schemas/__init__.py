from backend.adapters.pg.schemas.base import BaseSchema
from backend.adapters.pg.schemas.student import StudentSchema
from backend.adapters.pg.schemas.professor import ProfessorSchema
from backend.adapters.pg.schemas.presentation import PresentationSchema
from backend.adapters.pg.schemas.presentation_evaluation import (
    PresentationEvaluationSchema,
)


__all__ = [
    "BaseSchema",
    "StudentSchema",
    "ProfessorSchema",
    "PresentationSchema",
    "PresentationEvaluationSchema",
]
