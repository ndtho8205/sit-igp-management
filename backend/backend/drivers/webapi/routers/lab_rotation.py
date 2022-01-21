from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.entities import Professor
from backend.adapters.pg import lab_rotation_repository
from backend.entities.types import ID
from backend.usecases.inputs import (
    LabRotationEvaluationCreateInput,
    LabRotationEvaluationUpdateInput,
)
from backend.usecases.lab_rotation import (
    update_lab_rotation_evaluation,
    create_new_lab_rotation_evaluation,
)
from backend.adapters.webapi.responses import LabRotationEvaluationResponse
from backend.drivers.webapi.dependencies import get_db, authenticate_user
from backend.entities.evaluations.courses import LabRotationEvaluation


router = APIRouter()


@router.post(
    "/{presentation_id}",
    response_model=LabRotationEvaluationResponse,
)
def create(
    presentation_id: ID,
    inp: LabRotationEvaluationCreateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> LabRotationEvaluation:
    evaluation = create_new_lab_rotation_evaluation(
        presentation_id,
        inp,
        current_user,
        lab_rotation_repository,
        db_session,
    )

    return evaluation


@router.put(
    "/{presentation_id}",
    response_model=LabRotationEvaluationResponse,
)
def update_evaluation(
    presentation_id: ID,
    inp: LabRotationEvaluationUpdateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> LabRotationEvaluation:
    evaluation = update_lab_rotation_evaluation(
        presentation_id,
        inp,
        current_user,
        lab_rotation_repository,
        db_session,
    )

    return evaluation
