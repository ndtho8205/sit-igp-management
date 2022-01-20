from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.entities.types import (
    ID,
    Gender,
    LongStr,
    FullName,
    ShortStr,
    RatingScore,
    UniversityEmailStr,
)


class ProfessorCreateInput(BaseModel):
    full_name: FullName
    email: UniversityEmailStr
    is_verified: bool = False
    is_superuser: bool = False


class ProfessorUpdateInput(BaseModel):
    full_name: Optional[FullName]
    email: Optional[UniversityEmailStr]
    is_verified: Optional[bool]
    is_superuser: Optional[bool]


class StudentCreateInput(BaseModel):
    full_name: FullName
    admission_date: date

    email: Optional[UniversityEmailStr]
    gender: Optional[Gender]
    area_of_study: Optional[LongStr]

    supervisor_id: Optional[ID]
    advisor1_id: Optional[ID]
    advisor2_id: Optional[ID]


class StudentUpdateInput(BaseModel):
    full_name: Optional[FullName]
    admission_date: Optional[date]

    email: Optional[UniversityEmailStr]
    gender: Optional[Gender]
    area_of_study: Optional[LongStr]

    supervisor_id: Optional[ID]
    advisor1_id: Optional[ID]
    advisor2_id: Optional[ID]


class PresentationCreateInput(BaseModel):
    student_id: ID
    presentation_date: date

    presentation_length: Optional[ShortStr]

    session_chair_id: Optional[ID]
    reviewer1_id: Optional[ID]
    reviewer2_id: Optional[ID]
    reviewer3_id: Optional[ID]
    reviewer4_id: Optional[ID]


class PresentationUpdateInput(BaseModel):
    presentation_date: Optional[date]

    presentation_length: Optional[ShortStr]

    session_chair_id: Optional[ID]
    reviewer1_id: Optional[ID]
    reviewer2_id: Optional[ID]
    reviewer3_id: Optional[ID]
    reviewer4_id: Optional[ID]


class PresentationEvaluationCreateInput(BaseModel):
    presentation_id: ID
    reviewer_id: ID

    score_research_goal: RatingScore
    score_delivery: RatingScore
    score_visual_aid: RatingScore
    score_time: RatingScore
    score_qa_ability: RatingScore

    comment: Optional[LongStr]


class PresentationEvaluationUpdateInput(BaseModel):
    score_research_goal: Optional[RatingScore]
    score_delivery: Optional[RatingScore]
    score_visual_aid: Optional[RatingScore]
    score_time: Optional[RatingScore]
    score_qa: Optional[RatingScore]

    comment: Optional[LongStr]
