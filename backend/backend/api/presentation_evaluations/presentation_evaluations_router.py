from typing import List, Optional

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.api import presentations
from backend.core import types
from backend.dependencies import get_db
from backend.core.exceptions import ConflictError, NotFoundError, ValidationError
from backend.api.router_dependencies import get_superuser, get_normal_user
from backend.api.professors.professors_entities import Professor
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
def create_presentation_evaluation(
    create_dto: PresentationEvaluationCreateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> PresentationEvaluationSchema:
    _validate_create_request_body(db_session, create_dto)

    return service.create(db_session, create_dto)


@router.get("/", response_model=List[PresentationEvaluationResponseDto])
def find_all_presentation_evaluations(
    presentation_id: Optional[types.ID] = None,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_normal_user),
) -> List[PresentationEvaluationSchema]:
    if presentation_id is None:
        return service.find_all(db_session)

    return service.find_all_evaluations_per_presentation(db_session, presentation_id)


@router.get("/{evaluation_id}", response_model=PresentationEvaluationResponseDto)
def find_one_presentation_evaluation_by_id(
    evaluation_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_normal_user),
) -> PresentationEvaluationSchema:
    db_evaluation = service.find_one_by_id(db_session, evaluation_id)
    if db_evaluation is None:
        raise NotFoundError()
    return db_evaluation


@router.get("/{presentation_id}/{reviewer_id}", response_model=PresentationEvaluationResponseDto)
def find_one_presentation_evaluation_by_presentation_and_reviewer_id(
    presentation_id: types.ID,
    reviewer_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_normal_user),
) -> PresentationEvaluationSchema:
    db_evaluation = service.find_one_by_presentation_and_reviewer_id(
        db_session,
        presentation_id,
        reviewer_id,
    )
    if db_evaluation is None:
        raise NotFoundError()

    return db_evaluation


@router.put("/{evaluation_id}", response_model=PresentationEvaluationResponseDto)
def update_presentation_evaluation_by_id(
    evaluation_id: types.ID,
    update_dto: PresentationEvaluationUpdateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_normal_user),
) -> PresentationEvaluationSchema:
    db_evaluation = service.update_by_id(db_session, evaluation_id, update_dto)
    if db_evaluation is None:
        raise NotFoundError()

    return db_evaluation


@router.delete("/{evaluation_id}", response_model=None)
def remove(
    evaluation_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> None:
    db_evaluation = service.find_one_by_id(db_session, evaluation_id)
    if db_evaluation is None:
        raise NotFoundError()

    return service.remove_by_id(db_session, evaluation_id)


def _validate_create_request_body(
    db_session: Session,
    dto: PresentationEvaluationCreateDto,
) -> None:
    if (
        service.find_one_by_presentation_and_reviewer_id(
            db_session,
            dto.presentation_id,
            dto.reviewer_id,
        )
        is not None
    ):
        raise ConflictError("The reviewer was already evaluated.")

    error_list = []
    db_presentation = presentations.service.find_one_by_id(
        db_session,
        dto.presentation_id,
    )

    if db_presentation is None:
        error_list.append(("presentation_id", "The presentation was not found"))
    elif dto.reviewer_id not in [
        db_presentation.reviewer1_id,
        db_presentation.reviewer2_id,
        db_presentation.reviewer3_id,
        db_presentation.reviewer4_id,
        db_presentation.reviewer5_id,
    ]:
        error_list.append(
            (
                "reviewer_id",
                "The reviewer does not have access rights to evaluate the presentation",
            ),
        )

    if error_list:
        raise ValidationError(error_list)
