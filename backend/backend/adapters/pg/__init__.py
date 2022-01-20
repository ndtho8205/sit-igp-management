from backend.adapters.pg.student_repository_adapter import student_repository
from backend.adapters.pg.professor_repository_adapter import professor_repository
from backend.adapters.pg.presentation_repository_adapter import presentation_repository


__all__ = [
    "student_repository",
    "professor_repository",
    "presentation_repository",
]
