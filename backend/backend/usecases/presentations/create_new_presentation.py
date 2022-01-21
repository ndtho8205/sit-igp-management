from sqlalchemy.orm.session import Session

from backend.entities import Professor, Presentation
from backend.usecases.errors import ForbiddenError
from backend.usecases.inputs import PresentationCreateInput
from backend.usecases.validators import (
    validate_presentation_student,
    validate_presentation_reviewers,
)
from backend.usecases.repositories.student_repository import StudentRepository
from backend.usecases.repositories.professor_repository import ProfessorRepository
from backend.usecases.repositories.presentation_repository import PresentationRepository


def create_new_presentation(
    inp: PresentationCreateInput,
    current_user: Professor,
    student_repository: StudentRepository,
    professor_repository: ProfessorRepository,
    presentation_repository: PresentationRepository,
    db_session: Session,
) -> Presentation:
    if not current_user.is_superuser:
        raise ForbiddenError()

    validate_presentation_student(inp.student_id, student_repository, db_session)
    validate_presentation_reviewers(
        inp.session_chair_id,
        inp.reviewer1_id,
        inp.reviewer2_id,
        inp.reviewer3_id,
        inp.reviewer4_id,
        professor_repository,
        db_session,
    )

    presentation = presentation_repository.create(db_session, inp)
    return presentation
