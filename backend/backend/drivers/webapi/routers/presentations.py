from typing import List, Optional

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.entities import Professor, Presentation
from backend.usecases import (
    delete_presentation,
    list_all_presentations,
    create_new_presentation,
    update_presentation_info,
)
from backend.adapters.pg import (
    student_repository,
    professor_repository,
    presentation_repository,
)
from backend.entities.types import ID
from backend.usecases.inputs import PresentationCreateInput, PresentationUpdateInput
from backend.adapters.webapi.responses import PresentationResponse
from backend.drivers.webapi.dependencies import get_db, authenticate_user


router = APIRouter()


@router.post("/", response_model=PresentationResponse)
def create_presentation(
    inp: PresentationCreateInput,
    db_session: Session = Depends(get_db),
    current_user: Professor = Depends(authenticate_user),
) -> Presentation:
    presentation_repository.set_session(db_session)
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
