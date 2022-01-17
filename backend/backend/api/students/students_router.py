from typing import Any, List

from starlette import status
from sqlalchemy.orm import Session
from pydantic.error_wrappers import ErrorWrapper

from fastapi import Depends, APIRouter
from fastapi.exceptions import HTTPException, RequestValidationError

from backend.api import professors
from backend.core import types
from backend.dependencies import get_db
from backend.core.exceptions import ResourceNotFoundError
from backend.api.router_dependencies import get_superuser
from backend.api.students.students_dto import (
    BaseStudentDto,
    StudentCreateDto,
    StudentUpdateDto,
    StudentResponseDto,
)
from backend.api.students.students_schema import StudentSchema
from backend.api.students.students_service import service
from backend.api.professors.professors_entities import Professor


router = APIRouter()


@router.post("/", response_model=StudentResponseDto)
def create(
    create_dto: StudentCreateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> StudentSchema:
    if (
        create_dto.email is not None
        and service.find_one_by_email(
            db_session,
            create_dto.email,
        )
        is not None
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    _check_supervior_advisors_exists(db_session, create_dto)

    return service.create(db_session, create_dto)


@router.get("/", response_model=List[StudentResponseDto])
def find_all(
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> List[StudentSchema]:
    return service.find_all(db_session)


@router.get("/{student_id}", response_model=StudentResponseDto)
def find_one(
    student_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> Any:
    db_student = service.find_one_by_id(db_session, student_id)
    if db_student is None:
        raise ResourceNotFoundError("Student")
    return db_student


@router.put("/{student_id}", response_model=StudentResponseDto)
def update(
    student_id: types.ID,
    update_dto: StudentUpdateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> StudentSchema:
    db_student = service.find_one_by_id(db_session, student_id)
    if db_student is None:
        raise ResourceNotFoundError("Student")

    _check_supervior_advisors_exists(db_session, update_dto)

    return service.update(db_session, student_id, update_dto)


@router.delete("/{student_id}", response_model=None)
def remove(
    student_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> Any:
    db_student = service.find_one_by_id(db_session, student_id)
    if db_student is None:
        raise ResourceNotFoundError("Student")

    return service.remove(db_session, student_id)


def _check_supervior_advisors_exists(db_session: Session, obj: BaseStudentDto) -> None:
    error_list = []

    if (
        obj.supervisor_id is not None
        and professors.service.find_one_by_id(
            db_session,
            obj.supervisor_id,
        )
        is None
    ):
        error_list.append(
            ErrorWrapper(
                ValueError("The supervisor was not found"),
                loc=("body", "supervisor_id"),
            ),
        )

    if (
        obj.advisor1_id is not None
        and professors.service.find_one_by_id(db_session, obj.advisor1_id) is None
    ):
        error_list.append(
            ErrorWrapper(
                ValueError("The advisor was not found"),
                loc=("body", "advisor1_id"),
            ),
        )

    if (
        obj.advisor2_id is not None
        and professors.service.find_one_by_id(db_session, obj.advisor2_id) is None
    ):
        error_list.append(
            ErrorWrapper(
                ValueError("The advisor was not found"),
                loc=("body", "advisor2_id"),
            ),
        )

    if error_list:
        raise RequestValidationError(error_list)
