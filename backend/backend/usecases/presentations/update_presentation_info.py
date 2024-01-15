from sqlalchemy.orm.session import Session

from backend.entities import Professor, Presentation
from backend.entities.types import ID
from backend.usecases.errors import NotFoundError, ForbiddenError
from backend.usecases.inputs import PresentationUpdateInput
from backend.usecases.validators import validate_presentation_reviewers
from backend.usecases.repositories.professor_repository import ProfessorRepository
from backend.usecases.repositories.presentation_repository import PresentationRepository


def update_presentation_info(
    presentation_id: ID,
    inp: PresentationUpdateInput,
    current_user: Professor,
    professor_repository: ProfessorRepository,
    presentation_repository: PresentationRepository,
    db_session: Session,
) -> Presentation:
    if not current_user.is_superuser:
        #Normal user can update presentation_length
        if (
            inp.presentation_date or 
            inp.session_chair_id or 
            inp.reviewer1_id or 
            inp.reviewer2_id or 
            inp.reviewer3_id or 
            inp.reviewer4_id
        ):
            raise ForbiddenError()
    else:
        validate_presentation_reviewers(
            inp.session_chair_id,
            inp.reviewer1_id,
            inp.reviewer2_id,
            inp.reviewer3_id,
            inp.reviewer4_id,
            professor_repository,
            db_session,
        )

    presentation = presentation_repository.update(db_session, presentation_id, inp)
    if presentation is None:
        raise NotFoundError("presentation was not found")

    return presentation
