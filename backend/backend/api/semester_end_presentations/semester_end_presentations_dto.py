from typing import Optional

from pydantic import BaseModel

from .semester_end_presentations_entities import (
    SemesterEndPresentation,
    BaseSemesterEndPresentation,
)


class BaseSemesterEndPresentationDto(BaseModel):
    reviewer1_id: Optional[int]
    reviewer2_id: Optional[int]
    reviewer3_id: Optional[int]
    reviewer4_id: Optional[int]


class SemesterEndPresentationCreateDto(
    BaseSemesterEndPresentation,
    BaseSemesterEndPresentationDto,
):
    pass


class SemesterEndPresentationUpdateDto(BaseSemesterEndPresentationDto):
    presentation_length: Optional[str]


class SemesterEndPresentationResponseDto(SemesterEndPresentation):
    pass
