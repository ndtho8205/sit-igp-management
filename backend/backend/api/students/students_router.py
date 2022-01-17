from typing import List

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.api import professors
from backend.core import types
from backend.dependencies import get_db
from backend.core.exceptions import NotFoundError, ValidationError
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
def create_student(
    create_dto: StudentCreateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> StudentSchema:
    _validate_request_body(db_session, create_dto)

    return service.create(db_session, create_dto)


@router.get("/", response_model=List[StudentResponseDto])
def find_all_students(
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> List[StudentSchema]:
    return service.find_all(db_session)


@router.get("/{student_id}", response_model=StudentResponseDto)
def find_one_student_by_id(
    student_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> StudentSchema:
    db_student = service.find_one_by_id(db_session, student_id)
    if db_student is None:
        raise NotFoundError()
    return db_student


@router.put("/{student_id}", response_model=StudentResponseDto)
def update_student_by_id(
    student_id: types.ID,
    update_dto: StudentUpdateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> StudentSchema:
    _validate_request_body(db_session, update_dto)

    db_student = service.update_by_id(db_session, student_id, update_dto)
    if db_student is None:
        raise NotFoundError()

    return db_student


@router.delete("/{student_id}", response_model=None)
def remove(
    student_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> None:
    if service.find_one_by_id(db_session, student_id) is None:
        raise NotFoundError()

    return service.remove_by_id(db_session, student_id)


def _validate_request_body(db_session: Session, dto: BaseStudentDto) -> None:
    error_list = []

    if dto.email is not None and not service.is_email_unique(db_session, dto.email):
        error_list.append(("email", "Student's email was already registered"))

    if (
        dto.supervisor_id is not None
        and professors.service.find_one_by_id(db_session, dto.supervisor_id) is None
    ):
        error_list.append(("supervisor_id", "The supervisor was not found"))

    if (
        dto.advisor1_id is not None
        and professors.service.find_one_by_id(db_session, dto.advisor1_id) is None
    ):
        error_list.append(("advisor1_id", "The advisor was not found"))

    if (
        dto.advisor2_id is not None
        and professors.service.find_one_by_id(db_session, dto.advisor2_id) is None
    ):
        error_list.append(("advisor2_id", "The advisor was not found"))

    if error_list:
        raise ValidationError(error_list)
