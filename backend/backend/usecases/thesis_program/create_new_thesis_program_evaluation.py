from sqlalchemy.orm.session import Session

from backend.entities import Professor, ThesisProgramEvaluation
from backend.entities.types import ID
from backend.usecases.inputs import ThesisProgramEvaluationCreateInput
from backend.usecases.repositories import ThesisProgramRepository


def create_new_thesis_program_evaluation(
    presentation_id: ID,
    inp: ThesisProgramEvaluationCreateInput,
    current_user: Professor,
    thesis_program_repository: ThesisProgramRepository,
    db_session: Session,
) -> ThesisProgramEvaluation:
    evaluation = thesis_program_repository.create(db_session, presentation_id, inp)
    return evaluation
