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
    research_goal: RatingScore
    delivery: RatingScore
    visual_aid: RatingScore
    time: RatingScore
    qa_ability: RatingScore

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
