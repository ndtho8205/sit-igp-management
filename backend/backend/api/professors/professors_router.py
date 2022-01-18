from typing import List

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.core import types
from backend.dependencies import get_db
from backend.core.exceptions import NotFoundError, ValidationError
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
def create_professor(
    create_dto: ProfessorCreateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> ProfessorSchema:
    _validate_create_request_body(db_session, create_dto)

    return service.create(db_session, create_dto)


@router.get("/", response_model=List[ProfessorResponseDto])
def find_all_professors(
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> List[ProfessorSchema]:
    return service.find_all(db_session)


@router.get("/{professor_id}", response_model=ProfessorResponseDto)
def find_one_professor_by_id(
    professor_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> ProfessorSchema:
    db_professor = service.find_one_by_id(db_session, professor_id)
    if db_professor is None:
        raise NotFoundError()
    return db_professor


@router.put("/{professor_id}", response_model=ProfessorResponseDto)
def update_professor_by_id(
    professor_id: types.ID,
    update_dto: ProfessorUpdateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> ProfessorSchema:
    _validate_update_request_body(db_session, professor_id, update_dto)

    db_professor = service.update_by_id(db_session, professor_id, update_dto)
    if db_professor is None:
        raise NotFoundError()

    return db_professor


@router.delete("/{professor_id}", response_model=None)
def remove(
    professor_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> None:
    if service.find_one_by_id(db_session, professor_id) is None:
        raise NotFoundError()

    return service.remove_by_id(db_session, professor_id)


def _validate_create_request_body(db_session: Session, dto: ProfessorCreateDto) -> None:
    if not service.is_email_unique(db_session, dto.email):
        raise ValidationError([("email", "Professor's email was already registered")])


def _validate_update_request_body(
    db_session: Session,
    professor_id: types.ID,
    dto: ProfessorUpdateDto,
) -> None:
    if dto.email is None:
        return

    db_professor = service.find_one_by_email(db_session, dto.email)
    if db_professor is not None and professor_id != db_professor.id_:
        raise ValidationError([("email", "Professor's email was already registered")])
