from typing import List, Optional

from abc import ABC, abstractmethod

from sqlalchemy.orm.session import Session

from backend.entities.types import ID
from backend.usecases.inputs import (
    PresentationEvaluationCreateInput,
    PresentationEvaluationUpdateInput,
)
from backend.entities.evaluations.presentation import PresentationEvaluation


class PresentationEvaluationRepository(ABC):
    @abstractmethod
    def create(
        self,
        db_session: Session,
        presentation_id: ID,
        reviewer_id: ID,
        inp: PresentationEvaluationCreateInput,
    ) -> PresentationEvaluation:
        pass

    @abstractmethod
    def update(
        self,
        db_session: Session,
        presentation_id: ID,
        reviewer_id: ID,
        inp: PresentationEvaluationUpdateInput,
    ) -> Optional[PresentationEvaluation]:
        pass

    @abstractmethod
    def find_all(
        self,
        db_session: Session,
        reviewer_id: Optional[ID],
    ) -> List[PresentationEvaluation]:
        pass

    @abstractmethod
    def find_one_by_presentation_and_reviewer_id(
        self,
        db_session: Session,
        presentation_id: ID,
        reviewer_id: ID,
    ) -> Optional[PresentationEvaluation]:
        pass
