from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.errors import NotFoundError
from backend.usecases.inputs import LabRotationEvaluationUpdateInput
from backend.entities.evaluations.courses import LabRotationEvaluation
from backend.usecases.repositories.lab_rotation_repository import LabRotationRepository


def update_lab_rotation_evaluation(
    presentation_id: ID,
    inp: LabRotationEvaluationUpdateInput,
    current_user: Professor,
    lab_rotation_repository: LabRotationRepository,
    db_session: Session,
) -> LabRotationEvaluation:

    evaluation = lab_rotation_repository.update(
        db_session,
        presentation_id,
        inp,
    )

    if evaluation is None:
        raise NotFoundError("lab rotation evaluation was not found")

    return evaluation
