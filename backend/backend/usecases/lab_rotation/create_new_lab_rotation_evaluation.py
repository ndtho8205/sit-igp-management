from sqlalchemy.orm.session import Session

from backend.entities import Professor, LabRotationEvaluation
from backend.entities.types import ID
from backend.usecases.inputs import LabRotationEvaluationCreateInput
from backend.usecases.repositories import LabRotationRepository


def create_new_lab_rotation_evaluation(
    presentation_id: ID,
    inp: LabRotationEvaluationCreateInput,
    current_user: Professor,
    lab_rotation_repository: LabRotationRepository,
    db_session: Session,
) -> LabRotationEvaluation:
    evaluation = lab_rotation_repository.create(db_session, presentation_id, inp)
    return evaluation
