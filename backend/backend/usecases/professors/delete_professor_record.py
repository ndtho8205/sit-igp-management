from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.errors import ForbiddenError
from backend.usecases.repositories.professor_repository import ProfessorRepository


def delete_professor_record(
    professor_id: ID,
    current_user: Professor,
    professor_repository: ProfessorRepository,
    db_session: Session,
) -> None:
    if not current_user.is_superuser:
        raise ForbiddenError()

    professor_repository.delete(db_session, professor_id)
