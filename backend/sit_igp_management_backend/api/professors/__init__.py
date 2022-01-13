from sit_igp_management_backend.api.professors.professors_router import router
from sit_igp_management_backend.api.professors.professors_schema import ProfessorSchema
from sit_igp_management_backend.api.professors.professors_service import service


__all__ = [
    "router",
    "ProfessorSchema",
    "service",
]
