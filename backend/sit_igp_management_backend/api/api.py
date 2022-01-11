from fastapi import APIRouter

from .students import students_router
from .professors import professors_router


router = APIRouter()

router.include_router(
    professors_router.router,
    prefix="/professors",
    tags=["professors"],
)

router.include_router(
    students_router.router,
    prefix="/students",
    tags=["students"],
)
