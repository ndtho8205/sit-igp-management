from typing import List, Optional

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.entities import Professor, Presentation, PresentationEvaluation
from backend.adapters.pg import (
    student_repository,
    professor_repository,
    presentation_repository,
    presentation_evaluation_repository,
)
from backend.entities.types import ID
from backend.usecases.inputs import (
    PresentationCreateInput,
    PresentationUpdateInput,
    PresentationEvaluationCreateInput,
    PresentationEvaluationUpdateInput,
)
from backend.usecases.presentations import (
    delete_presentation,
    list_all_presentations,
    create_new_presentation,
    update_presentation_info,
)
from backend.adapters.webapi.responses import (
    PresentationResponse,
    PresentationEvaluationResponse,
)
from backend.drivers.webapi.dependencies import get_db, authenticate_user
from backend.usecases.presentation_evaluations import (
    update_presentation_evaluation,
    create_new_presentation_evaluation,
)


router = APIRouter()


@router.post("/", response_model=PresentationResponse)
def create_presentation(
    inp: PresentationCreateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> Presentation:
    presentation = create_new_presentation(
        inp,
        current_user,
        student_repository,
        professor_repository,
        presentation_repository,
        db_session,
    )

    return presentation


@router.get("/", response_model=List[PresentationResponse])
def find_all_presentations(
    reviewer_id: Optional[ID] = None,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> List[Presentation]:
    presentations = list_all_presentations(
        reviewer_id,
        current_user,
        presentation_repository,
        db_session,
    )
    return presentations


@router.put("/{presentation_id}", response_model=PresentationResponse)
def update_presentation_by_id(
    presentation_id: ID,
    inp: PresentationUpdateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> Presentation:
    presentation = update_presentation_info(
        presentation_id,
        inp,
        current_user,
        professor_repository,
        presentation_repository,
        db_session,
    )

    return presentation


@router.delete("/{presentation_id}", response_model=PresentationResponse)
def delete(
    presentation_id: ID,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> None:
    delete_presentation(
        presentation_id,
        current_user,
        presentation_repository,
        db_session,
    )


@router.post(
    "/{presentation_id}/evaluations/",
    response_model=PresentationEvaluationResponse,
)
def evaluate_presentation(
    presentation_id: ID,
    inp: PresentationEvaluationCreateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> PresentationEvaluation:
    evaluation = create_new_presentation_evaluation(
        inp,
        current_user,
        presentation_repository,
        presentation_evaluation_repository,
        db_session,
    )

    return evaluation


@router.put(
    "/{presentation_id}/evaluations/{reviewer_id}",
    response_model=PresentationEvaluationResponse,
)
def update_evaluation(
    presentation_id: ID,
    reviewer_id: ID,
    inp: PresentationEvaluationUpdateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> PresentationEvaluation:
    evaluation = update_presentation_evaluation(
        presentation_id,
        reviewer_id,
        inp,
        current_user,
        presentation_repository,
        presentation_evaluation_repository,
        db_session,
    )

    return evaluation
