from typing import List

from sqlalchemy.orm.session import Session

from backend.entities import Student, Professor
from backend.usecases.errors import ForbiddenError
from backend.usecases.repositories.student_repository import StudentRepository


def list_all_students(
    current_user: Professor,
    student_repository: StudentRepository,
    db_session: Session,
) -> List[Student]:
    if not current_user.is_superuser:
        raise ForbiddenError()

    return student_repository.find_all(db_session)
