from typing import List

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.entities import Professor
from backend.usecases import (
    get_semester_end_evaluation_summary,
    get_semester_end_evaluation_summary_by_supervisor_id,
)
from backend.adapters.pg import (
    lab_seminar_repository,
    lab_rotation_repository,
    presentation_repository,
    thesis_program_repository,
)
from backend.entities.types import ID
from backend.adapters.webapi.responses import SemesterEndEvaluationResponse
from backend.drivers.webapi.dependencies import get_db, authenticate_user
from backend.entities.semester_end_evaluation import SemesterEndEvaluation


router = APIRouter()


@router.get(
    "/",
    response_model=List[SemesterEndEvaluationResponse],
)
def get_summary(
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> List[SemesterEndEvaluation]:
    summary = get_semester_end_evaluation_summary(
        current_user,
        presentation_repository,
        thesis_program_repository,
        lab_seminar_repository,
        lab_rotation_repository,
        db_session,
    )

    return summary


@router.get(
    "/{supervisor_id}",
    response_model=List[SemesterEndEvaluationResponse],
)
def get_summary_by_supervisor_id(
    supervisor_id: ID,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> List[SemesterEndEvaluation]:
    summary = get_semester_end_evaluation_summary_by_supervisor_id(
        supervisor_id,
        current_user,
        presentation_repository,
        thesis_program_repository,
        lab_seminar_repository,
        lab_rotation_repository,
        db_session,
    )

    return summary
