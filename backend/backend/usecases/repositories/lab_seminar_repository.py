from typing import Optional

from abc import ABC, abstractmethod

from sqlalchemy.orm.session import Session

from backend.entities.types import ID
from backend.usecases.inputs import (
    LabSeminarEvaluationCreateInput,
    LabSeminarEvaluationUpdateInput,
)
from backend.entities.evaluations.courses import LabSeminarEvaluation


class LabSeminarRepository(ABC):
    @abstractmethod
    def create(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: LabSeminarEvaluationCreateInput,
    ) -> LabSeminarEvaluation:
        pass

    @abstractmethod
    def update(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: LabSeminarEvaluationUpdateInput,
    ) -> Optional[LabSeminarEvaluation]:
        pass

    @abstractmethod
    def find_one_by_presentation_id(
        self,
        db_session: Session,
        presentation_id: ID,
    ) -> Optional[LabSeminarEvaluation]:
        pass
