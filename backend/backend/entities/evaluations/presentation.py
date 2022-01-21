from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.entities.types import ID, RatingScore
from backend.entities.student import Student
from backend.entities.professor import Professor


class PresentationEvaluation(BaseModel):
    id_: ID

    score_research_goal: RatingScore
    score_delivery: RatingScore
    score_visual_aid: RatingScore
    score_time: RatingScore
    score_qa_ability: RatingScore

    question_score: float

    comment: Optional[str]

    class Config:
        orm_mode = True


class Presentation(BaseModel):
    id_: ID

    student: Student
    presentation_date: date

    presentation_length: Optional[str]
    session_chair: Optional[Professor]

    reviewer1: Optional[Professor]
    reviewer2: Optional[Professor]
    reviewer3: Optional[Professor]
    reviewer4: Optional[Professor]

    reviewer1_evaluation: Optional[PresentationEvaluation]
    reviewer2_evaluation: Optional[PresentationEvaluation]
    reviewer3_evaluation: Optional[PresentationEvaluation]
    reviewer4_evaluation: Optional[PresentationEvaluation]

    class Config:
        orm_mode = True

    @property
    def average_score(self) -> Optional[float]:
        reviewer_evaluations = [
            self.reviewer1_evaluation,
            self.reviewer2_evaluation,
            self.reviewer3_evaluation,
            self.reviewer4_evaluation,
        ]
        scores = []
        for evaluation in reviewer_evaluations:
            if evaluation is None:
                return None
            scores.append(evaluation.question_score)

        return sum(scores) / 4


def compute_presentation_question_score(
    score_research_goal: int,
    score_delivery: int,
    score_visual_aid: int,
    score_time: int,
    score_qa_ability: int,
) -> float:
    return (
        score_research_goal * 0.35
        + score_delivery * 0.2
        + score_visual_aid * 0.2
        + score_time * 0.05
        + score_qa_ability * 0.2
    ) * 20
