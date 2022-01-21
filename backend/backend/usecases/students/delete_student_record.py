from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.errors import ForbiddenError
from backend.usecases.repositories.student_repository import StudentRepository


def delete_student_record(
    student_id: ID,
    current_user: Professor,
    student_repository: StudentRepository,
    db_session: Session,
) -> None:
    if not current_user.is_superuser:
        raise ForbiddenError()

    student_repository.delete(db_session, student_id)
