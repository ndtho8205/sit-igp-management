from typing import Any

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter
from fastapi.exceptions import HTTPException

from sit_igp_management_backend.dependencies import get_db

from . import students_service
from .students_dto import CreateStudentDto, UpdateStudentDto


router = APIRouter()


@router.post("/")
def create(
    student: CreateStudentDto,
    db_session: Session = Depends(get_db),
) -> Any:
    return students_service.create(db_session, student)


@router.get("/")
def find_all(
    db_session: Session = Depends(get_db),
) -> Any:
    return students_service.find_all(db_session)


@router.get("/{student_id}")
def find_one(
    student_id: int,
    db_session: Session = Depends(get_db),
) -> Any:
    db_student = students_service.find_one_by_id(db_session, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student


@router.put("/{student_id}")
def update(
    student_id: int,
    update_student_dto: UpdateStudentDto,
    db_session: Session = Depends(get_db),
) -> Any:
    return students_service.update(db_session, student_id, update_student_dto)


@router.delete("/{student_id}")
def remove(
    student_id: int,
    db_session: Session = Depends(get_db),
) -> Any:
    return students_service.remove(db_session, student_id)
