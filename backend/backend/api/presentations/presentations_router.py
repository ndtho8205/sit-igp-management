from typing import List, Optional

from sqlalchemy.orm import Session
from pydantic.error_wrappers import ErrorWrapper

from fastapi import Depends, APIRouter
from fastapi.exceptions import RequestValidationError

from backend.api import students, professors
from backend.core import types
from backend.dependencies import get_db
from backend.core.exceptions import ResourceNotFoundError
from backend.api.presentations.presentations_dto import (
    BasePresentationDto,
    PresentationCreateDto,
    PresentationUpdateDto,
    PresentationResponseDto,
)
from backend.api.presentations.presentations_schema import PresentationSchema
from backend.api.presentations.presentations_service import service


router = APIRouter()


@router.post("/", response_model=PresentationResponseDto)
def create(
    create_dto: PresentationCreateDto,
    db_session: Session = Depends(get_db),
) -> PresentationSchema:
    _check_student_exists(db_session, create_dto.student_id)
    _check_reviewers_exists(db_session, create_dto)

    return service.create(db_session, create_dto)


@router.get("/", response_model=List[PresentationResponseDto])
def find_all(
    db_session: Session = Depends(get_db),
) -> List[PresentationSchema]:
    return service.find_all(db_session)


@router.get("/{presentation_id}", response_model=PresentationResponseDto)
def find_one(
    presentation_id: types.ID,
    db_session: Session = Depends(get_db),
) -> Optional[PresentationSchema]:
    db_presentation = service.find_one_by_id(db_session, presentation_id)
    if db_presentation is None:
        raise ResourceNotFoundError("semester end presentation")

    return db_presentation


@router.put("/{presentation_id}", response_model=PresentationResponseDto)
def update(
    presentation_id: types.ID,
    update_dto: PresentationUpdateDto,
    db_session: Session = Depends(get_db),
) -> PresentationSchema:
    db_presentation = service.find_one_by_id(db_session, presentation_id)
    if db_presentation is None:
        raise ResourceNotFoundError("semester end presentation")

    _check_reviewers_exists(db_session, update_dto)

    return service.update(db_session, presentation_id, update_dto)


@router.delete("/{presentation_id}", response_model=PresentationResponseDto)
def remove(
    presentation_id: types.ID,
    db_session: Session = Depends(get_db),
) -> None:
    db_presentation = service.find_one_by_id(db_session, presentation_id)
    if db_presentation is None:
        raise ResourceNotFoundError("semester end presentation")

    return service.remove(db_session, presentation_id)


def _check_student_exists(db_session: Session, student_id: types.ID) -> None:
    if students.service.find_one_by_id(db_session, student_id) is None:
        raise RequestValidationError(
            [
                ErrorWrapper(
                    ValueError("The student was not found"),
                    loc=("body", "student_id"),
                ),
            ],
        )


def _check_reviewers_exists(db_session: Session, obj: BasePresentationDto) -> None:
    error_list = []
    reviewers = {
        "1": obj.reviewer1_id,
        "2": obj.reviewer2_id,
        "3": obj.reviewer3_id,
        "4": obj.reviewer4_id,
        "5": obj.reviewer5_id,
    }

    for reviewer_role, reviewer_id in reviewers.items():
        if (
            reviewer_id is not None
            and professors.service.find_one_by_id(db_session, reviewer_id) is None
        ):
            error_list.append(
                ErrorWrapper(
                    ValueError(f"The reviewer {reviewer_role} was not found"),
                    loc=("body", f"reviewer{reviewer_role}_id"),
                )
            )

    if error_list:
        raise RequestValidationError(error_list)
