from backend.drivers.webapi.routers.students import router as students_router
from backend.drivers.webapi.routers.professors import router as professors_router
from backend.drivers.webapi.routers.lab_seminar import router as lab_seminar_router
from backend.drivers.webapi.routers.lab_rotation import router as lab_rotation_router
from backend.drivers.webapi.routers.presentations import router as presentations_router
from backend.drivers.webapi.routers.thesis_program import (
    router as thesis_program_router,
)
from backend.drivers.webapi.routers.semester_end_evaluation import (
    router as semester_end_evaluation_router,
)


__all__ = [
    "students_router",
    "professors_router",
    "presentations_router",
    "lab_seminar_router",
    "lab_rotation_router",
    "thesis_program_router",
    "semester_end_evaluation_router",
]
