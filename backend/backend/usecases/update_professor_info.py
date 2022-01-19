from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.errors import ConflictError, NotFoundError, ForbiddenError
from backend.usecases.inputs import ProfessorUpdateInput
from backend.usecases.repositories.professor_repository import ProfessorRepository


def update_professor_info(
    current_user: Professor,
    professor_repository: ProfessorRepository,
    professor_id: ID,
    inp: ProfessorUpdateInput,
) -> Professor:
    if not current_user.is_superuser:
        raise ForbiddenError()

    if inp.email is not None:
        existing_professor = professor_repository.find_one_by_email(inp.email)
        print(existing_professor)
        if existing_professor is not None and existing_professor.id_ != professor_id:
            raise ConflictError("email already exists")

    professor = professor_repository.update(professor_id, inp)
    if professor is None:
        raise NotFoundError("professor was not found")

    return professor
