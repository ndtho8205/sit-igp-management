from backend.usecases.repositories.student_repository import StudentRepository
from backend.usecases.repositories.professor_repository import ProfessorRepository
from backend.usecases.repositories.lab_seminar_repository import LabSeminarRepository
from backend.usecases.repositories.lab_rotation_repository import LabRotationRepository
from backend.usecases.repositories.presentation_repository import PresentationRepository
from backend.usecases.repositories.thesis_program_repository import (
    ThesisProgramRepository,
)
from backend.usecases.repositories.presentation_evaluation_repository import (
    PresentationEvaluationRepository,
)


__all__ = [
    "StudentRepository",
    "ProfessorRepository",
    "PresentationRepository",
    "PresentationEvaluationRepository",
    "ThesisProgramRepository",
    "LabSeminarRepository",
    "LabRotationRepository",
]
