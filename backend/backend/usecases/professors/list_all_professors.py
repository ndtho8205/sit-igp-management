from typing import List

from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.usecases.errors import ForbiddenError
from backend.usecases.repositories.professor_repository import ProfessorRepository


def list_all_professors(
    current_user: Professor,
    professor_repository: ProfessorRepository,
    db_session: Session,
) -> List[Professor]:
    if not current_user.is_superuser:
        raise ForbiddenError()

    return professor_repository.find_all(db_session)
