from sqlalchemy.orm.session import Session

from backend.entities import Professor, PresentationEvaluation
from backend.entities.types import ID
from backend.usecases.errors import NotFoundError
from backend.usecases.inputs import PresentationEvaluationUpdateInput
from backend.usecases.validators import validate_presentation_evaluation_reviewer_rights
from backend.usecases.repositories.presentation_repository import PresentationRepository
from backend.usecases.repositories.presentation_evaluation_repository import (
    PresentationEvaluationRepository,
)


def update_presentation_evaluation(
    presentation_id: ID,
    reviewer_id: ID,
    inp: PresentationEvaluationUpdateInput,
    current_user: Professor,
    presentation_repository: PresentationRepository,
    presentation_evaluation_repository: PresentationEvaluationRepository,
    db_session: Session,
) -> PresentationEvaluation:
    validate_presentation_evaluation_reviewer_rights(
        reviewer_id,
        current_user.id_,
        presentation_repository,
        presentation_evaluation_repository,
        db_session,
    )

    evaluation = presentation_evaluation_repository.update(
        db_session,
        presentation_id,
        reviewer_id,
        inp,
    )

    if evaluation is None:
        raise NotFoundError("presentation evaluation was not found")

    return evaluation
