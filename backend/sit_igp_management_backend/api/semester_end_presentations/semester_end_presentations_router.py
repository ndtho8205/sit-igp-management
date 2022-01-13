from typing import List, Optional

from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter

from sit_igp_management_backend.api import students, professors
from sit_igp_management_backend.dependencies import get_db
from sit_igp_management_backend.core.exceptions import ResourceNotFoundError

from .semester_end_presentations_dto import (
    BaseSemesterEndPresentationDto,
    SemesterEndPresentationCreateDto,
    SemesterEndPresentationUpdateDto,
    SemesterEndPresentationResponseDto,
)
from .semester_end_presentations_schema import SemesterEndPresentationsSchema
from .semester_end_presentations_service import service


router = APIRouter()


@router.post("/", response_model=SemesterEndPresentationResponseDto)
def create(
    create_dto: SemesterEndPresentationCreateDto,
    db_session: Session = Depends(get_db),
) -> SemesterEndPresentationsSchema:
    if not students.service.is_exists(db_session, create_dto.student_id):
        raise ResourceNotFoundError("Student")

    _check_reviewers_exists(db_session, create_dto)

    return service.create(db_session, create_dto)


@router.get("/", response_model=List[SemesterEndPresentationResponseDto])
def find_all(
    db_session: Session = Depends(get_db),
) -> List[SemesterEndPresentationsSchema]:
    return service.find_all(db_session)


@router.get("/{presentation_id}", response_model=SemesterEndPresentationResponseDto)
def find_one(
    presentation_id: int,
    db_session: Session = Depends(get_db),
) -> Optional[SemesterEndPresentationsSchema]:
    db_presentation = service.find_one_by_id(db_session, presentation_id)
    if db_presentation is None:
        raise ResourceNotFoundError("Presentation")

    return db_presentation


@router.put("/{presentation_id}", response_model=SemesterEndPresentationResponseDto)
def update(
    presentation_id: int,
    update_dto: SemesterEndPresentationUpdateDto,
    db_session: Session = Depends(get_db),
) -> SemesterEndPresentationsSchema:
    db_presentation = service.find_one_by_id(db_session, presentation_id)
    if db_presentation is None:
        raise ResourceNotFoundError("Presentation")

    _check_reviewers_exists(db_session, update_dto)

    return service.update(db_session, presentation_id, update_dto)


@router.delete("/{presentation_id}", response_model=SemesterEndPresentationResponseDto)
def remove(
    presentation_id: int,
    db_session: Session = Depends(get_db),
) -> None:
    db_presentation = service.find_one_by_id(db_session, presentation_id)
    if db_presentation is None:
        raise ResourceNotFoundError("Presentation")

    return service.remove(db_session, presentation_id)


def _check_reviewers_exists(
    db_session: Session, obj: BaseSemesterEndPresentationDto
) -> None:
    if not professors.service.is_exists(db_session, obj.reviewer1_id):
        raise ResourceNotFoundError("Reviewer 1")

    if not professors.service.is_exists(db_session, obj.reviewer2_id):
        raise ResourceNotFoundError("Reviewer 2")

    if not professors.service.is_exists(db_session, obj.reviewer3_id):
        raise ResourceNotFoundError("Reviewer 3")

    if not professors.service.is_exists(db_session, obj.reviewer4_id):
        raise ResourceNotFoundError("Reviewer 4")
