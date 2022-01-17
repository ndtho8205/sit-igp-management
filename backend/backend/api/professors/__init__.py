from backend.api.professors.professors_router import router
from backend.api.professors.professors_schema import ProfessorSchema
from backend.api.professors.professors_service import service


__all__ = [
    "router",
    "ProfessorSchema",
    "service",
]
