from typing import Optional

from abc import ABC, abstractmethod

from sqlalchemy.orm.session import Session

from backend.entities.types import ID
from backend.usecases.inputs import (
    LabRotationEvaluationCreateInput,
    LabRotationEvaluationUpdateInput,
)
from backend.entities.evaluations.courses import LabRotationEvaluation


class LabRotationRepository(ABC):
    @abstractmethod
    def create(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: LabRotationEvaluationCreateInput,
    ) -> LabRotationEvaluation:
        pass

    @abstractmethod
    def update(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: LabRotationEvaluationUpdateInput,
    ) -> Optional[LabRotationEvaluation]:
        pass

    @abstractmethod
    def find_one_by_presentation_id(
        self,
        db_session: Session,
        presentation_id: ID,
    ) -> Optional[LabRotationEvaluation]:
        pass
