from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.errors import ForbiddenError
from backend.usecases.repositories.presentation_repository import PresentationRepository


def delete_presentation(
    presentation_id: ID,
    current_user: Professor,
    presentation_repository: PresentationRepository,
    db_session: Session,
) -> None:
    if not current_user.is_superuser:
        raise ForbiddenError()

    presentation_repository.delete(db_session, presentation_id)
