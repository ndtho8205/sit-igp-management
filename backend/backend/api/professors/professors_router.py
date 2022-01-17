from typing import List

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter
from fastapi.exceptions import HTTPException

from backend.core import types
from backend.dependencies import get_db
from backend.core.exceptions import ResourceNotFoundError
from backend.api.router_dependencies import get_superuser
from backend.api.professors.professors_dto import (
    ProfessorCreateDto,
    ProfessorUpdateDto,
    ProfessorResponseDto,
)
from backend.api.professors.professors_schema import ProfessorSchema
from backend.api.professors.professors_service import service
from backend.api.professors.professors_entities import Professor


router = APIRouter()


@router.post("/", response_model=ProfessorResponseDto)
def create(
    create_dto: ProfessorCreateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> ProfessorSchema:
    db_professor = service.find_one_by_email(db_session, create_dto.email)
    if db_professor is not None:
        raise HTTPException(status_code=409, detail="Email already registered")

    return service.create(db_session, create_dto)


@router.get("/", response_model=List[ProfessorResponseDto])
def find_all(
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> List[ProfessorSchema]:
    return service.find_all(db_session)


@router.get("/{professor_id}", response_model=ProfessorResponseDto)
def find_one(
    professor_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> ProfessorSchema:
    db_professor = service.find_one_by_id(db_session, professor_id)
    if db_professor is None:
        raise ResourceNotFoundError("professor")
    return db_professor


@router.put("/{professor_id}", response_model=ProfessorResponseDto)
def update(
    professor_id: types.ID,
    update_dto: ProfessorUpdateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> ProfessorSchema:
    db_professor = service.find_one_by_id(db_session, professor_id)
    if db_professor is None:
        raise ResourceNotFoundError("professor")

    return service.update(db_session, professor_id, update_dto)


@router.delete("/{professor_id}", response_model=None)
def remove(
    professor_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> None:
    db_professor = service.find_one_by_id(db_session, professor_id)
    if db_professor is None:
        raise ResourceNotFoundError("professor")

    return service.remove(db_session, professor_id)
