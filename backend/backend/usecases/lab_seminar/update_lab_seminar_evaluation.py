from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.errors import NotFoundError
from backend.usecases.inputs import LabSeminarEvaluationUpdateInput
from backend.entities.evaluations.courses import LabSeminarEvaluation
from backend.usecases.repositories.lab_seminar_repository import LabSeminarRepository


def update_lab_seminar_evaluation(
    presentation_id: ID,
    inp: LabSeminarEvaluationUpdateInput,
    current_user: Professor,
    lab_seminar_repository: LabSeminarRepository,
    db_session: Session,
) -> LabSeminarEvaluation:

    evaluation = lab_seminar_repository.update(
        db_session,
        presentation_id,
        inp,
    )

    if evaluation is None:
        raise NotFoundError("lab seminar evaluation was not found")

    return evaluation
