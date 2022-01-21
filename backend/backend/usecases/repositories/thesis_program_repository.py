from typing import Optional

from abc import ABC, abstractmethod

from sqlalchemy.orm.session import Session

from backend.entities.types import ID
from backend.usecases.inputs import (
    ThesisProgramEvaluationCreateInput,
    ThesisProgramEvaluationUpdateInput,
)
from backend.entities.evaluations.courses import ThesisProgramEvaluation


class ThesisProgramRepository(ABC):
    @abstractmethod
    def create(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: ThesisProgramEvaluationCreateInput,
    ) -> ThesisProgramEvaluation:
        pass

    @abstractmethod
    def update(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: ThesisProgramEvaluationUpdateInput,
    ) -> Optional[ThesisProgramEvaluation]:
        pass

    @abstractmethod
    def find_one_by_presentation_id(
        self,
        db_session: Session,
        presentation_id: ID,
    ) -> Optional[ThesisProgramEvaluation]:
        pass
