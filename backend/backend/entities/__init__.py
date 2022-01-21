from backend.entities.student import Student
from backend.entities.professor import Professor
from backend.entities.evaluations.courses import (
    LabSeminarEvaluation,
    LabRotationEvaluation,
    ThesisProgramEvaluation,
)
from backend.entities.semester_end_evaluation import SemesterEndEvaluation
from backend.entities.evaluations.presentation import (
    Presentation,
    PresentationEvaluation,
    compute_presentation_question_score,
)


__all__ = [
    "Professor",
    "Student",
    "Presentation",
    "PresentationEvaluation",
    "compute_presentation_question_score",
    "LabSeminarEvaluation",
    "LabRotationEvaluation",
    "ThesisProgramEvaluation",
    "SemesterEndEvaluation",
]
