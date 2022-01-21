from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.usecases.errors import ConflictError, ForbiddenError
from backend.usecases.inputs import ProfessorCreateInput
from backend.usecases.repositories.professor_repository import ProfessorRepository


def create_new_professor_record(
    inp: ProfessorCreateInput,
    current_user: Professor,
    professor_repository: ProfessorRepository,
    db_session: Session,
) -> Professor:
    if not current_user.is_superuser:
        raise ForbiddenError()

    if professor_repository.find_one_by_email(db_session, inp.email) is not None:
        raise ConflictError("email already exists")

    professor = professor_repository.create(db_session, inp)
    return professor
