from sqlalchemy.orm.session import Session

from backend.entities import Professor, LabSeminarEvaluation
from backend.entities.types import ID
from backend.usecases.inputs import LabSeminarEvaluationCreateInput
from backend.usecases.repositories import LabSeminarRepository


def create_new_lab_seminar_evaluation(
    presentation_id: ID,
    inp: LabSeminarEvaluationCreateInput,
    current_user: Professor,
    lab_seminar_repository: LabSeminarRepository,
    db_session: Session,
) -> LabSeminarEvaluation:
    evaluation = lab_seminar_repository.create(db_session, presentation_id, inp)
    return evaluation
