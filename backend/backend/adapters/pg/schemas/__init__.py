from backend.adapters.pg.schemas.base import BaseSchema
from backend.adapters.pg.schemas.student import StudentSchema
from backend.adapters.pg.schemas.professor import ProfessorSchema
from backend.adapters.pg.schemas.presentation import PresentationSchema
from backend.adapters.pg.schemas.lab_seminar_evaluation import (
    LabSeminarEvaluationSchema,
)
from backend.adapters.pg.schemas.lab_rotation_evaluation import (
    LabRotationEvaluationSchema,
)
from backend.adapters.pg.schemas.presentation_evaluation import (
    PresentationEvaluationSchema,
)
from backend.adapters.pg.schemas.thesis_program_evaluation import (
    ThesisProgramEvaluationSchema,
)


__all__ = [
    "BaseSchema",
    "StudentSchema",
    "ProfessorSchema",
    "PresentationSchema",
    "PresentationEvaluationSchema",
    "LabSeminarEvaluationSchema",
    "LabRotationEvaluationSchema",
    "ThesisProgramEvaluationSchema",
]
