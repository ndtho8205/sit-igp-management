from typing import List

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.entities import Professor
from backend.usecases import (
    list_all_professors,
    update_professor_info,
    delete_professor_record,
    create_new_professor_record,
)
from backend.adapters.pg import professor_repository
from backend.entities.types import ID
from backend.usecases.inputs import ProfessorCreateInput, ProfessorUpdateInput
from backend.adapters.webapi.responses import ProfessorResponse
from backend.drivers.webapi.dependencies import get_db, authenticate_user


router = APIRouter()


@router.post("/", response_model=ProfessorResponse)
def create_professor(
    inp: ProfessorCreateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> ProfessorResponse:
    professor_repository.set_session(db_session)
    professor = create_new_professor_record(current_user, professor_repository, inp)

    return professor


@router.get("/", response_model=List[ProfessorResponse])
def find_all_professors(
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> List[ProfessorResponse]:
    professor_repository.set_session(db_session)
    professors = list_all_professors(current_user, professor_repository)

    return professors


@router.put("/{professor_id}", response_model=ProfessorResponse)
def update_professor_by_id(
    professor_id: ID,
    inp: ProfessorUpdateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> ProfessorResponse:
    professor_repository.set_session(db_session)
    db_professor = update_professor_info(
        current_user,
        professor_repository,
        professor_id,
        inp,
    )

    return db_professor


@router.delete("/{professor_id}", response_model=None, status_code=204)
def delete(
    professor_id: ID,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> None:
    professor_repository.set_session(db_session)
    delete_professor_record(
        current_user,
        professor_repository,
        professor_id,
    )
