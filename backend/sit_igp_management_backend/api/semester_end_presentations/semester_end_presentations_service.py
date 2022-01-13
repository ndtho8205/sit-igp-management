from sit_igp_management_backend.core.crud_base_service import CRUDBaseService

from .semester_end_presentations_dto import (
    SemesterEndPresentationCreateDto,
    SemesterEndPresentationUpdateDto,
)
from .semester_end_presentations_schema import SemesterEndPresentationsSchema


class SemesterEndPresentationsService(
    CRUDBaseService[
        SemesterEndPresentationsSchema,
        SemesterEndPresentationCreateDto,
        SemesterEndPresentationUpdateDto,
    ]
):
    pass


service = SemesterEndPresentationsService(SemesterEndPresentationsSchema)
