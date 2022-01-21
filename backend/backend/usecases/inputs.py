from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.entities.types import (
    ID,
    Score,
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

    question_score: Score

    comment: Optional[LongStr]


class PresentationEvaluationUpdateInput(BaseModel):
    score_research_goal: RatingScore
    score_delivery: RatingScore
    score_visual_aid: RatingScore
    score_time: RatingScore
    score_qa_ability: RatingScore

    question_score:Score

    comment: Optional[LongStr]


class ThesisProgramEvaluationCreateInput(BaseModel):
    presentation_id: ID

    score_daily_activities_1: Score
    score_daily_activities_2: Score
    score_meeting_presentation_1: Score
    score_meeting_presentation_2: Score

    course_score: Score


class ThesisProgramEvaluationUpdateInput(BaseModel):
    score_daily_activities_1: Score
    score_daily_activities_2: Score
    score_meeting_presentation_1: Score
    score_meeting_presentation_2: Score

    course_score: Score


class LabSeminarEvaluationCreateInput(BaseModel):
    presentation_id: ID

    score_daily_activities_1: Score
    score_daily_activities_2: Score
    score_meeting_presentation_1: Score
    score_meeting_presentation_2: Score

    course_score: Score


class LabSeminarEvaluationUpdateInput(BaseModel):
    score_daily_activities_1: Score
    score_daily_activities_2: Score
    score_meeting_presentation_1: Score
    score_meeting_presentation_2: Score

    course_score: Score


class LabRotationEvaluationCreateInput(BaseModel):
    presentation_id: ID

    course_score: Score


class LabRotationEvaluationUpdateInput(BaseModel):
    course_score: Score
