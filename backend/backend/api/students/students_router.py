from typing import Any, List

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter
from fastapi.exceptions import HTTPException

from backend.api import professors
from backend.dependencies import get_db
from backend.core.exceptions import ResourceNotFoundError
from backend.api.students.students_dto import (
    BaseStudentDto,
    StudentCreateDto,
    StudentUpdateDto,
    StudentResponseDto,
)
from backend.api.students.students_schema import StudentSchema
from backend.api.students.students_service import service


router = APIRouter()


@router.post("/", response_model=StudentResponseDto)
def create(
    create_dto: StudentCreateDto,
    db_session: Session = Depends(get_db),
) -> StudentSchema:
    if create_dto.email is not None and service.find_one_by_email(
        db_session,
        create_dto.email,
    ):
        raise HTTPException(status_code=409, detail="Email already registered")

    _check_supervior_advisors_exists(db_session, create_dto)

    return service.create(db_session, create_dto)


@router.get("/", response_model=List[StudentResponseDto])
def find_all(
    db_session: Session = Depends(get_db),
) -> List[StudentSchema]:
    return service.find_all(db_session)


@router.get("/{student_id}", response_model=StudentResponseDto)
def find_one(
    student_id: int,
    db_session: Session = Depends(get_db),
) -> Any:
    db_student = service.find_one_by_id(db_session, student_id)
    if db_student is None:
        raise ResourceNotFoundError("Student")
    return db_student


@router.put("/{student_id}", response_model=StudentResponseDto)
def update(
    student_id: int,
    update_dto: StudentUpdateDto,
    db_session: Session = Depends(get_db),
) -> StudentSchema:
    db_student = service.find_one_by_id(db_session, student_id)
    if db_student is None:
        raise ResourceNotFoundError("Student")

    _check_supervior_advisors_exists(db_session, update_dto)

    return service.update(db_session, student_id, update_dto)


@router.delete("/{student_id}", response_model=None)
def remove(
    student_id: int,
    db_session: Session = Depends(get_db),
) -> Any:
    db_student = service.find_one_by_id(db_session, student_id)
    if db_student is None:
        raise ResourceNotFoundError("Student")

    return service.remove(db_session, student_id)


def _check_supervior_advisors_exists(db_session: Session, obj: BaseStudentDto) -> None:
    if not professors.service.is_exists(db_session, obj.supervisor_id):
        raise ResourceNotFoundError("Supervisor")

    if not professors.service.is_exists(db_session, obj.advisor1_id):
        raise ResourceNotFoundError("Advisor 1")

    if not professors.service.is_exists(db_session, obj.advisor2_id):
        raise ResourceNotFoundError("Advisor 2")
