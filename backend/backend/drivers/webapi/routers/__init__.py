from backend.drivers.webapi.routers.students import router as students_router
from backend.drivers.webapi.routers.professors import router as professors_router
from backend.drivers.webapi.routers.presentations import router as presentations_router


__all__ = [
    "students_router",
    "professors_router",
    "presentations_router",
]
