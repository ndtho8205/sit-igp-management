from backend.drivers.webapi.routers.students import router as students_router
from backend.drivers.webapi.routers.professors import router as professors_router


__all__ = [
    "students_router",
    "professors_router",
]
