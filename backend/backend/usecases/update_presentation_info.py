from backend.entities import Professor, Presentation
from backend.entities.types import ID
from backend.usecases.errors import NotFoundError, ForbiddenError
from backend.usecases.inputs import PresentationUpdateInput
from backend.usecases.validators import validate_presentation_reviewers
from backend.usecases.repositories.professor_repository import ProfessorRepository
from backend.usecases.repositories.presentation_repository import PresentationRepository


def update_presentation_info(
    current_user: Professor,
    professor_repository: ProfessorRepository,
    presentation_repository: PresentationRepository,
    presentation_id: ID,
    inp: PresentationUpdateInput,
) -> Presentation:
    if not current_user.is_superuser:
        raise ForbiddenError()

    validate_presentation_reviewers(
        professor_repository,
        inp.session_chair_id,
        inp.reviewer1_id,
        inp.reviewer2_id,
        inp.reviewer3_id,
        inp.reviewer4_id,
    )

    presentation = presentation_repository.update(presentation_id, inp)
    if presentation is None:
        raise NotFoundError("presentation was not found")

    return presentation
