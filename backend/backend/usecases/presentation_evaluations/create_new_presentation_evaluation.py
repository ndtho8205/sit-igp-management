from sqlalchemy.orm.session import Session

from backend.entities import Professor, PresentationEvaluation
from backend.usecases.inputs import PresentationEvaluationCreateInput
from backend.usecases.validators import validate_presentation_evaluation_reviewer_rights
from backend.usecases.repositories.presentation_repository import PresentationRepository
from backend.usecases.repositories.presentation_evaluation_repository import (
    PresentationEvaluationRepository,
)


def create_new_presentation_evaluation(
    inp: PresentationEvaluationCreateInput,
    current_user: Professor,
    presentation_repository: PresentationRepository,
    presentation_evaluation_repository: PresentationEvaluationRepository,
    db_session: Session,
) -> PresentationEvaluation:
    validate_presentation_evaluation_reviewer_rights(
        current_user.id_,
        inp.reviewer_id,
        presentation_repository,
        presentation_evaluation_repository,
        db_session,
    )

    evaluation = presentation_evaluation_repository.create(
        db_session,
        inp.presentation_id,
        inp.reviewer_id,
        inp,
    )
    return evaluation
