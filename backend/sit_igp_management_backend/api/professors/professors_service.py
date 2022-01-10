from typing import Any

from sqlalchemy.orm import Session

from .professors_dto import CreateProfessorDto, UpdateProfessorDto
from .professors_schema import ProfessorSchema


def create(
    db_session: Session,
    create_professor_dto: CreateProfessorDto,
) -> Any:
    db_professor = ProfessorSchema(**create_professor_dto.dict())
    db_session.add(db_professor)
    db_session.commit()
    db_session.refresh(db_professor)

    return db_professor


def find_all(
    db_session: Session,
) -> Any:
    return db_session.query(ProfessorSchema).all()


def find_one_by_id(
    db_session: Session,
    professor_id: int,
) -> Any:
    return (
        db_session.query(ProfessorSchema)
        .filter(ProfessorSchema.professor_id == professor_id)
        .first()
    )


def find_one_by_email(
    db_session: Session,
    professor_email: str,
) -> Any:
    return (
        db_session.query(ProfessorSchema)
        .filter(ProfessorSchema.email == professor_email)
        .first()
    )


def update(
    db_session: Session,
    professor_id: int,
    update_professor_dto: UpdateProfessorDto,
) -> Any:
    raise NotImplementedError()


def remove(
    db_session: Session,
    professor_id: int,
) -> Any:
    raise NotImplementedError()
