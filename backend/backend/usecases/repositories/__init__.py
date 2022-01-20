from backend.usecases.repositories.student_repository import StudentRepository
from backend.usecases.repositories.professor_repository import ProfessorRepository
from backend.usecases.repositories.presentation_repository import PresentationRepository
from backend.usecases.repositories.presentation_evaluation_repository import (
    PresentationEvaluationRepository,
)


__all__ = [
    "StudentRepository",
    "ProfessorRepository",
    "PresentationRepository",
    "PresentationEvaluationRepository",
]
