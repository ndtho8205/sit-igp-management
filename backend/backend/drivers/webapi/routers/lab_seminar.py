from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.entities import Professor
from backend.adapters.pg import lab_seminar_repository
from backend.entities.types import ID
from backend.usecases.inputs import (
    LabSeminarEvaluationCreateInput,
    LabSeminarEvaluationUpdateInput,
)
from backend.usecases.lab_seminar import (
    update_lab_seminar_evaluation,
    create_new_lab_seminar_evaluation,
)
from backend.adapters.webapi.responses import LabSeminarEvaluationResponse
from backend.drivers.webapi.dependencies import get_db, authenticate_user
from backend.entities.evaluations.courses import LabSeminarEvaluation


router = APIRouter()


@router.post(
    "/{presentation_id}",
    response_model=LabSeminarEvaluationResponse,
)
def create(
    presentation_id: ID,
    inp: LabSeminarEvaluationCreateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> LabSeminarEvaluation:
    evaluation = create_new_lab_seminar_evaluation(
        presentation_id,
        inp,
        current_user,
        lab_seminar_repository,
        db_session,
    )

    return evaluation


@router.put(
    "/{presentation_id}",
    response_model=LabSeminarEvaluationResponse,
)
def update_evaluation(
    presentation_id: ID,
    inp: LabSeminarEvaluationUpdateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> LabSeminarEvaluation:
    evaluation = update_lab_seminar_evaluation(
        presentation_id,
        inp,
        current_user,
        lab_seminar_repository,
        db_session,
    )

    return evaluation
