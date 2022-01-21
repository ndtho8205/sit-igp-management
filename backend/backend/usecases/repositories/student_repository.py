from typing import List, Optional

from abc import ABC, abstractmethod

from sqlalchemy.orm.session import Session

from backend.entities import Student
from backend.entities.types import ID
from backend.usecases.inputs import StudentCreateInput, StudentUpdateInput


class StudentRepository(ABC):
    @abstractmethod
    def create(self, db_session: Session, inp: StudentCreateInput) -> Student:
        pass

    @abstractmethod
    def update(
        self, db_session: Session, student_id: ID, inp: StudentUpdateInput
    ) -> Optional[Student]:
        pass

    @abstractmethod
    def delete(self, db_session: Session, student_id: ID) -> None:
        pass

    @abstractmethod
    def find_all(
        self,
        db_session: Session,
    ) -> List[Student]:
        pass

    @abstractmethod
    def find_one_by_id(self, db_session: Session, student_id: ID) -> Optional[Student]:
        pass

    @abstractmethod
    def find_one_by_email(self, db_session: Session, email: str) -> Optional[Student]:
        pass
