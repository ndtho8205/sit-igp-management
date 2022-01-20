from backend.entities import Professor
from backend.usecases.errors import ConflictError, ForbiddenError
from backend.usecases.inputs import ProfessorCreateInput
from backend.usecases.repositories.professor_repository import ProfessorRepository


def create_new_professor_record(
    current_user: Professor,
    professor_repository: ProfessorRepository,
    inp: ProfessorCreateInput,
) -> Professor:
    if not current_user.is_superuser:
        raise ForbiddenError()

    if professor_repository.find_one_by_email(inp.email) is not None:
        raise ConflictError("email already exists")

    professor = professor_repository.create(inp)
    return professor
