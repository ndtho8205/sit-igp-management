from typing import List

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.entities import Student, Professor
from backend.usecases import (
    list_all_students,
    update_student_info,
    delete_student_record,
    create_new_student_record,
)
from backend.adapters.pg import student_repository, professor_repository
from backend.entities.types import ID
from backend.usecases.inputs import StudentCreateInput, StudentUpdateInput
from backend.adapters.webapi.responses import StudentResponse
from backend.drivers.webapi.dependencies import get_db, authenticate_user


router = APIRouter()


@router.post("/", response_model=StudentResponse)
def create_student(
    inp: StudentCreateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> Student:
    student_repository.set_session(db_session)
    student = create_new_student_record(
        current_user,
        student_repository,
        professor_repository,
        inp,
    )

    return student


@router.get("/", response_model=List[StudentResponse])
def find_all_students(
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> List[Student]:
    student_repository.set_session(db_session)
    students = list_all_students(current_user, student_repository)

    return students


@router.put("/{student_id}", response_model=StudentResponse)
def update_student_by_id(
    student_id: ID,
    inp: StudentUpdateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> Student:
    student_repository.set_session(db_session)
    student = update_student_info(
        current_user,
        student_repository,
        professor_repository,
        student_id,
        inp,
    )

    return student


@router.delete("/{student_id}", response_model=None, status_code=204)
def delete(
    student_id: ID,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> None:
    student_repository.set_session(db_session)
    delete_student_record(
        current_user,
        student_repository,
        student_id,
    )