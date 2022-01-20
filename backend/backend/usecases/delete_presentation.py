from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.errors import ForbiddenError
from backend.usecases.repositories.presentation_repository import PresentationRepository


def delete_presentation(
    current_user: Professor,
    presentation_repository: PresentationRepository,
    presentation_id: ID,
) -> None:
    if not current_user.is_superuser:
        raise ForbiddenError()

    presentation_repository.delete(presentation_id)
