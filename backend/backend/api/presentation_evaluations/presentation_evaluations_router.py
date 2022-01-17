from typing import List, Optional

from starlette import status
from sqlalchemy.orm import Session
from pydantic.error_wrappers import ErrorWrapper

from fastapi import Depends, APIRouter
from fastapi.exceptions import HTTPException, RequestValidationError

from backend.api import presentations
from backend.core import types
from backend.dependencies import get_db
from backend.core.exceptions import ResourceNotFoundError
from backend.api.router_dependencies import get_superuser, get_normal_user
from backend.api.professors.professors_entities import Professor
from backend.api.presentations.presentations_schema import PresentationSchema
from backend.api.presentations.presentations_service import (
    service as presentations_service,
)
from backend.api.presentation_evaluations.presentation_evaluations_dto import (
    PresentationEvaluationCreateDto,
    PresentationEvaluationUpdateDto,
    PresentationEvaluationResponseDto,
)
from backend.api.presentation_evaluations.presentation_evaluations_schema import (
    PresentationEvaluationSchema,
)
from backend.api.presentation_evaluations.presentation_evaluations_service import (
    service,
)


router = APIRouter()


@router.post("/", response_model=PresentationEvaluationResponseDto)
def create(
    create_dto: PresentationEvaluationCreateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> PresentationEvaluationSchema:
    db_presentation = presentations_service.find_one_by_id(
        db_session,
        create_dto.presentation_id,
    )
    if db_presentation is None:
        raise ResourceNotFoundError("semester end presentation")

    _check_reviewer_evaluation_permission(
        db_presentation,
        create_dto.reviewer_id,
    )

    db_evaluation = service.find_one_by_presentation_reviewer_id(
        db_session, db_presentation.id_, create_dto.reviewer_id
    )
    if db_evaluation is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The reviewer's evaluation already exists.",
        )

    return service.create(db_session, create_dto)


@router.get("/{presentation_id}", response_model=List[PresentationEvaluationResponseDto])
def find_all_evaluations_per_presentation(
    presentation_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_normal_user),
) -> List[PresentationEvaluationSchema]:
    return service.find_all_evaluations_per_presentation(db_session, presentation_id)


@router.get(
    "/",
    response_model=PresentationEvaluationResponseDto,
)
def find_one(
    presentation_id: types.ID,
    reviewer_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_normal_user),
) -> Optional[PresentationEvaluationSchema]:
    db_evaluation = service.find_one_by_presentation_reviewer_id(
        db_session,
        presentation_id,
        reviewer_id,
    )
    if db_evaluation is None:
        raise ResourceNotFoundError("reviewer's evaluation")

    return db_evaluation


@router.put("/{evaluation_id}", response_model=PresentationEvaluationResponseDto)
def update(
    evaluation_id: types.ID,
    update_dto: PresentationEvaluationUpdateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_normal_user),
) -> PresentationEvaluationSchema:
    db_evaluation = service.find_one_by_id(db_session, evaluation_id)
    if db_evaluation is None:
        raise ResourceNotFoundError("reviewer's evaluation")

    return service.update(db_session, evaluation_id, update_dto)


@router.delete("/{presentation_id}", response_model=PresentationEvaluationResponseDto)
def remove(
    presentation_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> None:
    db_presentation = service.find_one_by_id(db_session, presentation_id)
    if db_presentation is None:
        raise ResourceNotFoundError("reviewer's evaluation")

    return service.remove(db_session, presentation_id)


def _check_presentation_exists(db_session: Session, presentation_id: types.ID) -> None:
    presentation = presentations.service.find_one_by_id(db_session, presentation_id)
    if not presentation:
        raise RequestValidationError(
            [
                ErrorWrapper(
                    ValueError("The presentation was not found"),
                    loc=("body", "presentation_id"),
                ),
            ],
        )


def _check_reviewer_evaluation_permission(
    presentation: PresentationSchema,
    reviewer_id: types.ID,
) -> None:
    if reviewer_id not in [
        presentation.reviewer1_id,
        presentation.reviewer2_id,
        presentation.reviewer3_id,
        presentation.reviewer4_id,
        presentation.reviewer5_id,
    ]:
        raise RequestValidationError(
            [
                ErrorWrapper(
                    ValueError("The presentation's reviewer was not found"),
                    loc=("body", "reviewer_id"),
                ),
            ],
        )
