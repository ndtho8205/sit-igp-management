from backend.entities.student import Student
from backend.entities.professor import Professor

# from backend.entities.evaluations.courses import (
#     LabSeminar,
#     LabRotation,
#     ThesisProgram,
#     SupervisorScore,
# )
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
    # "LabSeminar",
    # "LabRotation",
    # "ThesisProgram",
    # "SupervisorScore",
]
