from typing import List, Optional

from backend.entities import Professor, Presentation
from backend.entities.types import ID
from backend.usecases.errors import ForbiddenError
from backend.usecases.repositories.presentation_repository import PresentationRepository


def list_all_presentations(
    current_user: Professor,
    presentation_repository: PresentationRepository,
    reviewer_id: Optional[ID],
) -> List[Presentation]:
    if not current_user.is_superuser:
        raise ForbiddenError()

    return presentation_repository.find_all(reviewer_id)
