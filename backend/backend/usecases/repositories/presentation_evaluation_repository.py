from typing import List, Optional

from abc import ABC, abstractmethod

from backend.entities.types import ID
from backend.usecases.inputs import (
    PresentationEvaluationCreateInput,
    PresentationEvaluationUpdateInput,
)
from backend.entities.evaluations.presentation import (
    Presentation,
    PresentationEvaluation,
)


class PresentationEvaluationRepository(ABC):
    @abstractmethod
    def create(
        self,
        inp: PresentationEvaluationCreateInput,
        question_score: float,
    ) -> PresentationEvaluation:
        pass

    @abstractmethod
    def update_by_presentation_and_reviewer_id(
        self,
        presentation_id: ID,
        reviewer_id: ID,
        inp: PresentationEvaluationUpdateInput,
        question_score: float,
    ) -> Optional[PresentationEvaluation]:
        pass

    @abstractmethod
    def delete(self, evaluation_id: ID) -> None:
        pass

    @abstractmethod
    def find_all(
        self,
        reviewer_id: Optional[ID],
    ) -> List[PresentationEvaluation]:
        pass
