from sqlalchemy.orm.session import Session

from backend.entities import Student, Professor
from backend.entities.types import ID
from backend.usecases.errors import ConflictError, NotFoundError, ForbiddenError
from backend.usecases.inputs import StudentUpdateInput
from backend.usecases.validators import validate_student_supervisor_advisor_exists
from backend.usecases.repositories.student_repository import StudentRepository
from backend.usecases.repositories.professor_repository import ProfessorRepository


def update_student_info(
    student_id: ID,
    inp: StudentUpdateInput,
    current_user: Professor,
    student_repository: StudentRepository,
    professor_repository: ProfessorRepository,
    db_session: Session,
) -> Student:
    if not current_user.is_superuser:
        raise ForbiddenError()

    if inp.email is not None:
        existing_student = student_repository.find_one_by_email(db_session, inp.email)
        if existing_student is not None and existing_student.id_ != student_id:
            raise ConflictError("email already exists")

    validate_student_supervisor_advisor_exists(
        inp.supervisor_id,
        inp.advisor1_id,
        inp.advisor2_id,
        professor_repository,
        db_session,
    )

    student = student_repository.update(db_session, student_id, inp)
    if student is None:
        raise NotFoundError("student was not found")

    return student
