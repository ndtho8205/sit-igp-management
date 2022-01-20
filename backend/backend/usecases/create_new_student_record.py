from backend.entities import Student, Professor
from backend.usecases.errors import ConflictError, ForbiddenError
from backend.usecases.inputs import StudentCreateInput
from backend.usecases.validators import validate_student_supervisor_advisor_exists
from backend.usecases.repositories.student_repository import StudentRepository
from backend.usecases.repositories.professor_repository import ProfessorRepository


def create_new_student_record(
    current_user: Professor,
    student_repository: StudentRepository,
    professor_repository: ProfessorRepository,
    inp: StudentCreateInput,
) -> Student:
    if not current_user.is_superuser:
        raise ForbiddenError()

    if (
        inp.email is not None
        and student_repository.find_one_by_email(inp.email) is not None
    ):
        raise ConflictError("email already exists")

    validate_student_supervisor_advisor_exists(
        professor_repository,
        inp.supervisor_id,
        inp.advisor1_id,
        inp.advisor2_id,
    )

    student = student_repository.create(inp)
    return student
