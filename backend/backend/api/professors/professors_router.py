from typing import List

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter
from fastapi.exceptions import HTTPException

from backend.dependencies import get_db
from backend.core.exceptions import ResourceNotFoundError
from backend.api.professors.professors_dto import (
    ProfessorCreateDto,
    ProfessorUpdateDto,
    ProfessorResponseDto,
)
from backend.api.professors.professors_schema import ProfessorSchema
from backend.api.professors.professors_service import service


router = APIRouter()


@router.post("/", response_model=ProfessorResponseDto)
def create(
    create_dto: ProfessorCreateDto,
    db_session: Session = Depends(get_db),
) -> ProfessorSchema:
    db_professor = service.find_one_by_email(db_session, create_dto.email)
    if db_professor:
        raise HTTPException(status_code=409, detail="Email already registered")

    return service.create(db_session, create_dto)


@router.get("/", response_model=List[ProfessorResponseDto])
def find_all(
    db_session: Session = Depends(get_db),
) -> List[ProfessorSchema]:
    return service.find_all(db_session)


@router.get("/{professor_id}", response_model=ProfessorResponseDto)
def find_one(
    professor_id: int,
    db_session: Session = Depends(get_db),
) -> ProfessorSchema:
    db_professor = service.find_one_by_id(db_session, professor_id)
    if db_professor is None:
        raise ResourceNotFoundError("Professor")
    return db_professor


@router.put("/{professor_id}", response_model=ProfessorResponseDto)
def update(
    professor_id: int,
    update_dto: ProfessorUpdateDto,
    db_session: Session = Depends(get_db),
) -> ProfessorSchema:
    db_professor = service.find_one_by_id(db_session, professor_id)
    if db_professor is None:
        raise ResourceNotFoundError("Professor")

    return service.update(db_session, professor_id, update_dto)


@router.delete("/{professor_id}", response_model=None)
def remove(
    professor_id: int,
    db_session: Session = Depends(get_db),
) -> None:
    db_professor = service.find_one_by_id(db_session, professor_id)
    if db_professor is None:
        raise ResourceNotFoundError("Professor")

    return service.remove(db_session, professor_id)
