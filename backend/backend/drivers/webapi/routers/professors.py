from typing import List

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.entities import Professor
from backend.adapters.pg import professor_repository
from backend.entities.types import ID
from backend.usecases.inputs import ProfessorCreateInput, ProfessorUpdateInput
from backend.usecases.professors import (
    list_all_professors,
    update_professor_info,
    delete_professor_record,
    create_new_professor_record,
)
from backend.adapters.webapi.responses import ProfessorResponse
from backend.drivers.webapi.dependencies import get_db, authenticate_user


router = APIRouter()


@router.post("/", response_model=ProfessorResponse)
def create_professor(
    inp: ProfessorCreateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> Professor:
    professor = create_new_professor_record(
        inp,
        current_user,
        professor_repository,
        db_session,
    )

    return professor


@router.get("/", response_model=List[ProfessorResponse])
def find_all_professors(
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> List[Professor]:
    professors = list_all_professors(current_user, professor_repository, db_session)

    return professors


@router.put("/{professor_id}", response_model=ProfessorResponse)
def update_professor_by_id(
    professor_id: ID,
    inp: ProfessorUpdateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> Professor:
    db_professor = update_professor_info(
        professor_id,
        inp,
        current_user,
        professor_repository,
        db_session,
    )

    return db_professor


@router.delete("/{professor_id}", response_model=None, status_code=204)
def delete(
    professor_id: ID,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> None:
    delete_professor_record(
        professor_id,
        current_user,
        professor_repository,
        db_session,
    )
