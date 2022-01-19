from typing import Optional

from backend.entities.types import ID
from backend.usecases.errors import NotFoundError
from backend.usecases.repositories.professor_repository import ProfessorRepository


def validate_student_supervisor_advisor_exists(
    professor_repository: ProfessorRepository,
    supervisor_id: Optional[ID],
    advisor1_id: Optional[ID],
    advisor2_id: Optional[ID],
) -> None:
    if (
        supervisor_id is not None
        and professor_repository.find_one_by_id(supervisor_id) is None
    ):
        raise NotFoundError("supervisor was not found")

    if (
        advisor1_id is not None
        and professor_repository.find_one_by_id(advisor1_id) is None
    ):
        raise NotFoundError("advisor 1 was not found")

    if (
        advisor2_id is not None
        and professor_repository.find_one_by_id(advisor2_id) is None
    ):
        raise NotFoundError("advisor 2 was not found")
