from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.entities import Student, Professor
from backend.entities.types import (
    ID,
    Score,
    Gender,
    LongStr,
    FullName,
    RatingScore,
    UniversityEmailStr,
)
from backend.entities.evaluations.courses import ThesisProgramEvaluation


class _SubProfessor(BaseModel):
    id_: ID
    full_name: str
    email: str


class ProfessorResponse(Professor):
    pass


class StudentResponse(BaseModel):
    id_: ID
    full_name: FullName
    admission_date: date

    email: Optional[UniversityEmailStr]
    gender: Optional[Gender]
    area_of_study: Optional[LongStr]

    supervisor: Optional[_SubProfessor]
    advisor1: Optional[_SubProfessor]
    advisor2: Optional[_SubProfessor]


class PresentationEvaluationResponse(BaseModel):
    score_research_goal: RatingScore
    score_delivery: RatingScore
    score_visual_aid: RatingScore
    score_time: RatingScore
    score_qa_ability: RatingScore

    comment: Optional[str]

    question_score: Optional[Score]


class PresentationResponse(BaseModel):
    id_: ID

    student: StudentResponse
    presentation_date: date
    presentation_length: Optional[str]

    session_chair: Optional[_SubProfessor]
    reviewer1: Optional[_SubProfessor]
    reviewer2: Optional[_SubProfessor]
    reviewer3: Optional[_SubProfessor]
    reviewer4: Optional[_SubProfessor]

    reviewer1_evaluation: Optional[PresentationEvaluationResponse]
    reviewer2_evaluation: Optional[PresentationEvaluationResponse]
    reviewer3_evaluation: Optional[PresentationEvaluationResponse]
    reviewer4_evaluation: Optional[PresentationEvaluationResponse]


class ThesisProgramEvaluationResponse(BaseModel):
    score_daily_activities_1: Score
    score_daily_activities_2: Score
    score_meeting_presentation_1: Score
    score_meeting_presentation_2: Score
    course_score: Score


class LabSeminarEvaluationResponse(BaseModel):
    score_daily_activities_1: Score
    score_daily_activities_2: Score
    score_meeting_presentation_1: Score
    score_meeting_presentation_2: Score
    course_score: Score


class LabRotationEvaluationResponse(BaseModel):
    course_score: Score


class SemesterEndEvaluationResponse(BaseModel):
    presentation: Optional[PresentationResponse]
    thesis_program: Optional[ThesisProgramEvaluationResponse]
    lab_seminar: Optional[LabSeminarEvaluationResponse]
    lab_rotation: Optional[LabRotationEvaluationResponse]

    class Config:
        orm_mode = True
