from typing import Optional

from sqlalchemy.orm.session import Session

from backend.entities.types import ID
from backend.usecases.errors import NotFoundError, ForbiddenError
from backend.usecases.repositories.student_repository import StudentRepository
from backend.usecases.repositories.professor_repository import ProfessorRepository
from backend.usecases.repositories.presentation_repository import PresentationRepository
from backend.usecases.repositories.presentation_evaluation_repository import (
    PresentationEvaluationRepository,
)


def validate_student_supervisor_advisor_exists(
    supervisor_id: Optional[ID],
    advisor1_id: Optional[ID],
    advisor2_id: Optional[ID],
    professor_repository: ProfessorRepository,
    db_session: Session,
) -> None:
    if (
        supervisor_id is not None
        and professor_repository.find_one_by_id(db_session, supervisor_id) is None
    ):
        raise NotFoundError("supervisor was not found")

    if (
        advisor1_id is not None
        and professor_repository.find_one_by_id(db_session, advisor1_id) is None
    ):
        raise NotFoundError("advisor 1 was not found")

    if (
        advisor2_id is not None
        and professor_repository.find_one_by_id(db_session, advisor2_id) is None
    ):
        raise NotFoundError("advisor 2 was not found")


def validate_presentation_student(
    student_id: ID,
    student_repository: StudentRepository,
    db_session: Session,
) -> None:
    if student_repository.find_one_by_id(db_session, student_id) is None:
        raise NotFoundError("student was not found")


def validate_presentation_reviewers(
    session_chair_id: Optional[ID],
    reviewer1_id: Optional[ID],
    reviewer2_id: Optional[ID],
    reviewer3_id: Optional[ID],
    reviewer4_id: Optional[ID],
    professor_repository: ProfessorRepository,
    db_session: Session,
) -> None:
    reviewers = {
        "session chair": session_chair_id,
        "reviewer 1": reviewer1_id,
        "reviewer 2": reviewer2_id,
        "reviewer 3": reviewer3_id,
        "reviewer 4": reviewer4_id,
    }
    for reviewer_role, reviewer_id in reviewers.items():
        if (
            reviewer_id is not None
            and professor_repository.find_one_by_id(db_session, reviewer_id) is None
        ):
            raise NotFoundError(f"{reviewer_role} was not found")


def validate_presentation_evaluation_reviewer_rights(
    reviewer_id: ID,
    current_user_id: ID,
    presentation_repository: PresentationRepository,
    presentation_evaluation_repository: PresentationEvaluationRepository,
    db_session: Session,
) -> None:
    if current_user_id != reviewer_id:
        raise ForbiddenError()
