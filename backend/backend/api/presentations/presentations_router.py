from typing import List, Union

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from backend.api import students, professors
from backend.core import types
from backend.dependencies import get_db
from backend.core.exceptions import NotFoundError, ValidationError
from backend.api.router_dependencies import get_superuser
from backend.api.professors.professors_entities import Professor
from backend.api.presentations.presentations_dto import (
    PresentationCreateDto,
    PresentationUpdateDto,
    PresentationResponseDto,
)
from backend.api.presentations.presentations_schema import PresentationSchema
from backend.api.presentations.presentations_service import service


router = APIRouter()


@router.post("/", response_model=PresentationResponseDto)
def create_presentation(
    create_dto: PresentationCreateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> PresentationSchema:
    _validate_request_body(db_session, create_dto)

    return service.create(db_session, create_dto)


@router.get("/", response_model=List[PresentationResponseDto])
def find_all_presentations(
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> List[PresentationSchema]:
    return service.find_all(db_session)


@router.get("/{presentation_id}", response_model=PresentationResponseDto)
def find_one_presentation_by_id(
    presentation_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> PresentationSchema:
    db_presentation = service.find_one_by_id(db_session, presentation_id)
    if db_presentation is None:
        raise NotFoundError()

    return db_presentation


@router.put("/{presentation_id}", response_model=PresentationResponseDto)
def update_presentation_by_id(
    presentation_id: types.ID,
    update_dto: PresentationUpdateDto,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> PresentationSchema:
    _validate_request_body(db_session, update_dto)

    db_presentation = service.update_by_id(db_session, presentation_id, update_dto)
    if db_presentation is None:
        raise NotFoundError()

    return db_presentation


@router.delete("/{presentation_id}", response_model=PresentationResponseDto)
def remove(
    presentation_id: types.ID,
    db_session: Session = Depends(get_db),
    _: Professor = Depends(get_superuser),
) -> None:
    if service.find_one_by_id(db_session, presentation_id) is None:
        raise NotFoundError()

    return service.remove_by_id(db_session, presentation_id)


def _validate_request_body(
    db_session: Session,
    dto: Union[PresentationCreateDto, PresentationUpdateDto],
) -> None:
    error_list = []

    if (
        dto.student_id is not None
        and students.service.find_one_by_id(db_session, dto.student_id) is None
    ):
        error_list.append(("student_id", "The student was not found"))

    reviewers = {
        "1": dto.reviewer1_id,
        "2": dto.reviewer2_id,
        "3": dto.reviewer3_id,
        "4": dto.reviewer4_id,
        "5": dto.reviewer5_id,
    }
    for reviewer_role, reviewer_id in reviewers.items():
        if (
            reviewer_id is not None
            and professors.service.find_one_by_id(db_session, reviewer_id) is None
        ):
            error_list.append(
                (
                    f"reviewer{reviewer_role}_id",
                    f"The reviewer {reviewer_role} was not found",
                )
            )

    if error_list:
        raise ValidationError(error_list)
