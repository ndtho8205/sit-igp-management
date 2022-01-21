from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.errors import NotFoundError
from backend.usecases.inputs import ThesisProgramEvaluationUpdateInput
from backend.entities.evaluations.courses import ThesisProgramEvaluation
from backend.usecases.repositories.thesis_program_repository import (
    ThesisProgramRepository,
)


def update_thesis_program_evaluation(
    presentation_id: ID,
    inp: ThesisProgramEvaluationUpdateInput,
    current_user: Professor,
    thesis_program_repository: ThesisProgramRepository,
    db_session: Session,
) -> ThesisProgramEvaluation:

    evaluation = thesis_program_repository.update(
        db_session,
        presentation_id,
        inp,
    )

    if evaluation is None:
        raise NotFoundError("thesis program evaluation was not found")

    return evaluation
