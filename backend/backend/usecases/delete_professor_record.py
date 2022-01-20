from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.errors import ForbiddenError
from backend.usecases.repositories.professor_repository import ProfessorRepository


def delete_professor_record(
    current_user: Professor,
    professor_repository: ProfessorRepository,
    professor_id: ID,
) -> None:
    if not current_user.is_superuser:
        raise ForbiddenError()

    professor_repository.delete(professor_id)
