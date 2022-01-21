from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.entities import Professor
from backend.adapters.pg import thesis_program_repository
from backend.entities.types import ID
from backend.usecases.inputs import (
    ThesisProgramEvaluationCreateInput,
    ThesisProgramEvaluationUpdateInput,
)
from backend.usecases.thesis_program import (
    update_thesis_program_evaluation,
    create_new_thesis_program_evaluation,
)
from backend.adapters.webapi.responses import ThesisProgramEvaluationResponse
from backend.drivers.webapi.dependencies import get_db, authenticate_user
from backend.entities.evaluations.courses import ThesisProgramEvaluation


router = APIRouter()


@router.post(
    "/{presentation_id}",
    response_model=ThesisProgramEvaluationResponse,
)
def create(
    presentation_id: ID,
    inp: ThesisProgramEvaluationCreateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> ThesisProgramEvaluation:
    evaluation = create_new_thesis_program_evaluation(
        presentation_id,
        inp,
        current_user,
        thesis_program_repository,
        db_session,
    )

    return evaluation


@router.put(
    "/{presentation_id}",
    response_model=ThesisProgramEvaluationResponse,
)
def update_evaluation(
    presentation_id: ID,
    inp: ThesisProgramEvaluationUpdateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> ThesisProgramEvaluation:
    evaluation = update_thesis_program_evaluation(
        presentation_id,
        inp,
        current_user,
        thesis_program_repository,
        db_session,
    )

    return evaluation
