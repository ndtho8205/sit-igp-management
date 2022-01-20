from typing import List, Optional

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.entities import Professor, Presentation, PresentationEvaluation
from backend.usecases import (
    delete_presentation,
    list_all_presentations,
    create_new_presentation,
    update_presentation_info,
    create_new_presentation_evaluation,
)
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
)
from backend.adapters.webapi.responses import (
    PresentationResponse,
    PresentationEvaluationResponse,
)
from backend.drivers.webapi.dependencies import get_db, authenticate_user


router = APIRouter()


@router.post("/", response_model=PresentationResponse)
def create_presentation(
    inp: PresentationCreateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> Presentation:
    presentation_repository.set_session(db_session)
    professor_repository.set_session(db_session)
    student_repository.set_session(db_session)
    presentation = create_new_presentation(
        current_user,
        student_repository,
        professor_repository,
        presentation_repository,
        inp,
    )

    return presentation


@router.get("/", response_model=List[PresentationResponse])
def find_all_presentations(
    reviewer_id: Optional[ID] = None,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> List[Presentation]:
    presentation_repository.set_session(db_session)
    presentations = list_all_presentations(
        current_user,
        presentation_repository,
        reviewer_id,
    )
    return presentations


@router.put("/{presentation_id}", response_model=PresentationResponse)
def update_presentation_by_id(
    presentation_id: ID,
    inp: PresentationUpdateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> Presentation:
    presentation_repository.set_session(db_session)
    professor_repository.set_session(db_session)
    presentation = update_presentation_info(
        current_user,
        professor_repository,
        presentation_repository,
        presentation_id,
        inp,
    )

    return presentation


@router.delete("/{presentation_id}", response_model=PresentationResponse)
def delete(
    presentation_id: ID,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> None:
    presentation_repository.set_session(db_session)
    delete_presentation(current_user, presentation_repository, presentation_id)


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
    presentation_repository.set_session(db_session)
    presentation_evaluation_repository.set_session(db_session)
    presentation_repository.set_session(db_session)

    evaluation = create_new_presentation_evaluation(
        current_user,
        presentation_repository,
        presentation_evaluation_repository,
        inp,
    )
    print(evaluation)

    return evaluation
