from typing import List, Optional

from abc import ABC, abstractmethod

from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.inputs import ProfessorCreateInput, ProfessorUpdateInput


class ProfessorRepository(ABC):
    @abstractmethod
    def create(self, db_session: Session, inp: ProfessorCreateInput) -> Professor:
        pass

    @abstractmethod
    def update(
        self,
        db_session: Session,
        professor_id: ID,
        inp: ProfessorUpdateInput,
    ) -> Optional[Professor]:
        pass

    @abstractmethod
    def delete(self, db_session: Session, professor_id: ID) -> None:
        pass

    @abstractmethod
    def find_all(self, db_session: Session) -> List[Professor]:
        pass

    @abstractmethod
    def find_one_by_id(
        self,
        db_session: Session,
        professor_id: ID,
    ) -> Optional[Professor]:
        pass

    @abstractmethod
    def find_one_by_email(self, db_session: Session, email: str) -> Optional[Professor]:
        pass
