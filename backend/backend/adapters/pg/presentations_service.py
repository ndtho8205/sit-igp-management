from backend.core.crud_base_service import CRUDBaseService
from backend.api.presentations.presentations_dto import (
    PresentationCreateDto,
    PresentationUpdateDto,
)
from backend.api.presentations.presentations_schema import PresentationSchema


class PresentationsService(
    CRUDBaseService[PresentationSchema, PresentationCreateDto, PresentationUpdateDto],
):
    pass


service = PresentationsService(PresentationSchema)
