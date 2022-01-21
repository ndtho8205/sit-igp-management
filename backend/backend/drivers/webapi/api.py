from typing import Dict

from fastapi import APIRouter
from fastapi.param_functions import Depends

from backend.entities.professor import Professor
from backend.drivers.webapi.routers import (
    students_router,
    professors_router,
    lab_seminar_router,
    lab_rotation_router,
    presentations_router,
    thesis_program_router,
    semester_end_evaluation_router,
)
from backend.drivers.webapi.dependencies import authenticate_user


router = APIRouter()


@router.get("/status", tags=["API Status"])
def root() -> Dict[str, str]:
    return {"status": "Ok"}


@router.get("/whoami", tags=["User"], response_model=Professor)
def whoami(current_user: Professor = Depends(authenticate_user)) -> Professor:
    return current_user


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
    tags=["Semester End Evaluation"],
)

router.include_router(
    thesis_program_router,
    prefix="/thesis_program",
    tags=["Semester End Evaluation"],
)

router.include_router(
    lab_seminar_router,
    prefix="/lab_seminar",
    tags=["Semester End Evaluation"],
)

router.include_router(
    lab_rotation_router,
    prefix="/lab_rotation",
    tags=["Semester End Evaluation"],
)

router.include_router(
    semester_end_evaluation_router,
    prefix="/summary",
    tags=["Semester End Evaluation"],
)
