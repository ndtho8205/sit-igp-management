from sit_igp_management_backend.api.students.students_router import router
from sit_igp_management_backend.api.students.students_schema import StudentSchema
from sit_igp_management_backend.api.students.students_service import service


__all__ = [
    "router",
    "StudentSchema",
    "service",
]
