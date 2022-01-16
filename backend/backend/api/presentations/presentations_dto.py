from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.core import types
from backend.api.presentations.presentations_entities import (
    Presentation,
    BasePresentation,
)


class BasePresentationDto(BaseModel):
    presentation_length: Optional[str]

    reviewer1_id: Optional[types.ID]
    reviewer2_id: Optional[types.ID]
    reviewer3_id: Optional[types.ID]
    reviewer4_id: Optional[types.ID]
    reviewer5_id: Optional[types.ID]


class PresentationCreateDto(BasePresentation, BasePresentationDto):
    pass


class PresentationUpdateDto(BasePresentationDto):
    is_deleted: Optional[bool]

    presentation_date: Optional[date]


class PresentationResponseDto(Presentation):
    pass
