from typing import Dict

from fastapi import APIRouter

from backend.api.students import students_router
from backend.api.professors import professors_router
from backend.api.presentations import presentations_router
from backend.api.presentation_evaluations import presentation_evaluations_router


router = APIRouter()


@router.get("/status", tags=["API Status"])
def root() -> Dict[str, str]:
    return {"status": "Ok"}


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
    presentations_router.router,
    prefix="/presentations",
    tags=["Semester End Presentation Information"],
)

router.include_router(
    presentation_evaluations_router.router,
    prefix="/presentation_evaluations",
    tags=["Semester End Presentation Evaluations"],
)
