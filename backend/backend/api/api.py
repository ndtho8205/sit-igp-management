from fastapi import APIRouter

from backend.api.students import students_router
from backend.api.professors import professors_router
from backend.api.semester_end_presentations import semester_end_presentations_router


router = APIRouter()

router.include_router(
    professors_router.router,
    prefix="/professors",
    tags=["Professors"],
)

router.include_router(
    students_router.router,
    prefix="/students",
    tags=["Students"],
)

router.include_router(
    semester_end_presentations_router.router,
    prefix="/semester_end_presentations",
    tags=["Semester End Presentation Information"],
)
