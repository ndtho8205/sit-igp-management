from backend.adapters.pg.schemas.base import BaseSchema
from backend.adapters.pg.schemas.student import StudentSchema
from backend.adapters.pg.schemas.professor import ProfessorSchema


__all__ = [
    "BaseSchema",
    "ProfessorSchema",
    "StudentSchema",
]
