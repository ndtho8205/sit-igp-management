from typing import Optional

from sqlalchemy.orm.session import Session

from backend.usecases.inputs import ProfessorUpdateInput
from backend.entities.professor import Professor
from backend.usecases.repositories.professor_repository import ProfessorRepository


def verify_professor_email(
    email: str,
    professor_repository: ProfessorRepository,
    db_session: Session,
) -> Optional[Professor]:
    professor = professor_repository.find_one_by_email(db_session, email)

    if professor is None:
        return None

    if not professor.is_verified:
        inp = ProfessorUpdateInput(is_verified=True)
        professor_repository.update(db_session, professor.id_, inp)

    return professor
