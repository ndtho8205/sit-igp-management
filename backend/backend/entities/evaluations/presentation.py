from typing import Tuple, Optional

from datetime import date

from pydantic import BaseModel

from backend.entities.types import RatingScore
from backend.entities.professor import Professor


class SemesterEndPresentationReviewerScore(BaseModel):
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


class SemesterEndPresentation(BaseModel):
    presentation_date: date

    presentation_length: Optional[str]
    session_chair: Optional[Professor]

    reviewer_1_evaluation: Tuple[
        Professor,
        Optional[SemesterEndPresentationReviewerScore],
    ]
    reviewer_2_evaluation: Tuple[
        Professor,
        Optional[SemesterEndPresentationReviewerScore],
    ]
    reviewer_3_evaluation: Tuple[
        Professor,
        Optional[SemesterEndPresentationReviewerScore],
    ]
    reviewer_4_evaluation: Tuple[
        Professor,
        Optional[SemesterEndPresentationReviewerScore],
    ]

    @property
    def average_score(self) -> Optional[float]:
        reviewer_evaluations = [
            self.reviewer_1_evaluation[1],
            self.reviewer_2_evaluation[1],
            self.reviewer_3_evaluation[1],
            self.reviewer_4_evaluation[1],
        ]
        scores = []
        for evaluation in reviewer_evaluations:
            if evaluation is None:
                return None
            scores.append(evaluation.question_score)

        return sum(scores) / 4
