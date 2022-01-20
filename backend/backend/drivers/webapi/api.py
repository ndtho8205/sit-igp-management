from typing import Dict

from fastapi import APIRouter

from backend.drivers.webapi.routers import (
    students_router,
    professors_router,
    presentations_router,
)


router = APIRouter()


@router.get("/status", tags=["API Status"])
def root() -> Dict[str, str]:
    return {"status": "Ok"}


router.include_router(
    professors_router,
    prefix="/professors",
    tags=["Professors"],
)

router.include_router(
    students_router,
    prefix="/students",
    tags=["Students"],
)

router.include_router(
    presentations_router,
    prefix="/presentations",
    tags=["Semester End Presentation Information"],
)
#
# router.include_router(
#    presentation_evaluations_router.router,
#    prefix="/presentation_evaluations",
#    tags=["Semester End Presentation Evaluations"],
# )
