from typing import Any

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter
from fastapi.exceptions import HTTPException

from sit_igp_management_backend.dependencies import get_db

from . import professors_service
from .professors_dto import CreateProfessorDto, UpdateProfessorDto


router = APIRouter(prefix="/professors", tags=["Professors"])


@router.post("/")
def create(
    professor: CreateProfessorDto,
    db_session: Session = Depends(get_db),
) -> Any:
    db_professor = professors_service.find_one_by_email(db_session, professor.email)
    if db_professor:
        raise HTTPException(status_code=400, detail="Email already registered")
    return professors_service.create(db_session, professor)


@router.get("/")
def find_all(
    db_session: Session = Depends(get_db),
) -> Any:
    return professors_service.find_all(db_session)


@router.get("/{professor_id}")
def find_one(
    professor_id: int,
    db_session: Session = Depends(get_db),
) -> Any:
    db_professor = professors_service.find_one_by_id(db_session, professor_id)
    if db_professor is None:
        raise HTTPException(status_code=404, detail="Professor not found")
    return db_professor


@router.put("/{professor_id}")
def update(
    professor_id: int,
    update_professor_dto: UpdateProfessorDto,
    db_session: Session = Depends(get_db),
) -> Any:
    return professors_service.update(db_session, professor_id, update_professor_dto)


@router.delete("/{professor_id}")
def remove(
    professor_id: int,
    db_session: Session = Depends(get_db),
) -> Any:
    return professors_service.remove(db_session, professor_id)
