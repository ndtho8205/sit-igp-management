from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.api.presentations.presentations_entities import (
    Presentation,
    BasePresentation,
)


class BasePresentationDto(BaseModel):
    presentation_length: Optional[str]

    reviewer1_id: Optional[int]
    reviewer2_id: Optional[int]
    reviewer3_id: Optional[int]
    reviewer4_id: Optional[int]
    reviewer5_id: Optional[int]


class PresentationCreateDto(BasePresentation, BasePresentationDto):
    pass


class PresentationUpdateDto(BasePresentationDto):
    is_deleted: Optional[bool]

    presentation_date: Optional[date]


class PresentationResponseDto(Presentation):
    pass
