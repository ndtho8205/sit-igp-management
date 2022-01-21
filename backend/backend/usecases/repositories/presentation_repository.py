from typing import List, Optional

from abc import ABC, abstractmethod

from sqlalchemy.orm.session import Session

from backend.entities.types import ID
from backend.usecases.inputs import PresentationCreateInput, PresentationUpdateInput
from backend.entities.evaluations.presentation import Presentation


class PresentationRepository(ABC):
    @abstractmethod
    def create(self, db_session: Session, inp: PresentationCreateInput) -> Presentation:
        pass

    @abstractmethod
    def update(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: PresentationUpdateInput,
    ) -> Optional[Presentation]:
        pass

    @abstractmethod
    def delete(self, db_session: Session, presentation_id: ID) -> None:
        pass

    @abstractmethod
    def find_all(
        self,
        db_session: Session,
        reviewer_id: Optional[ID]=None,
    ) -> List[Presentation]:
        pass

    @abstractmethod
    def find_one_by_id(
        self,
        db_session: Session,
        presentation_id: ID,
    ) -> Optional[Presentation]:
        pass
