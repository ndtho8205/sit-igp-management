from typing import Optional

from datetime import date

from pydantic import BaseModel

from backend.entities.types import ID, RatingScore
from backend.entities.student import Student
from backend.entities.professor import Professor


class PresentationReviewerEvaluation(BaseModel):
    id_: ID

    research_goal: RatingScore
    delivery: RatingScore
    visual_aid: RatingScore
    time: RatingScore
    qa_ability: RatingScore

    comment: Optional[str]

    @property
    def question_score(self) -> float:
        return (
            self.research_goal * 0.35
            + self.delivery * 0.2
            + self.visual_aid * 0.2
            + self.time * 0.05
            + self.qa_ability * 0.2
        ) * 20


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

    reviewer1_evaluation: Optional[PresentationReviewerEvaluation]
    reviewer2_evaluation: Optional[PresentationReviewerEvaluation]
    reviewer3_evaluation: Optional[PresentationReviewerEvaluation]
    reviewer4_evaluation: Optional[PresentationReviewerEvaluation]

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
