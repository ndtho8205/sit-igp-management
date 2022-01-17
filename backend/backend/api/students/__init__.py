from backend.api.students.students_router import router
from backend.api.students.students_schema import StudentSchema
from backend.api.students.students_service import service


__all__ = [
    "router",
    "StudentSchema",
    "service",
]
