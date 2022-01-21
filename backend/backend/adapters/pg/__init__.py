from backend.adapters.pg.student_repository_adapter import student_repository
from backend.adapters.pg.professor_repository_adapter import professor_repository
from backend.adapters.pg.lab_seminar_repository_adapter import lab_seminar_repository
from backend.adapters.pg.lab_rotation_repository_adapter import lab_rotation_repository
from backend.adapters.pg.presentation_repository_adapter import presentation_repository
from backend.adapters.pg.thesis_program_repository_adapter import (
    thesis_program_repository,
)
from backend.adapters.pg.presentation_evaluation_repository_adapter import (
    presentation_evaluation_repository,
)


__all__ = [
    "student_repository",
    "professor_repository",
    "presentation_repository",
    "presentation_evaluation_repository",
    "thesis_program_repository",
    "lab_seminar_repository",
    "lab_rotation_repository",
]
