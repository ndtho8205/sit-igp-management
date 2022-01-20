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
    PresentationReviewerEvaluation,
)


__all__ = [
    "Professor",
    "Student",
    "Presentation",
    "PresentationReviewerEvaluation",
    # "LabSeminar",
    # "LabRotation",
    # "ThesisProgram",
    # "SupervisorScore",
]
