from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.errors import ForbiddenError
from backend.usecases.repositories.student_repository import StudentRepository


def delete_student_record(
    current_user: Professor,
    student_repository: StudentRepository,
    student_id: ID,
) -> None:
    if not current_user.is_superuser:
        raise ForbiddenError()

    student_repository.delete(student_id)
