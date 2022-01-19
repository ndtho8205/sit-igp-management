from typing import List, Optional

from abc import ABC, abstractmethod

from backend.entities import Student
from backend.usecases.inputs import StudentCreateInput, StudentUpdateInput
from backend.usecases.validators import ID


class StudentRepository(ABC):
    @abstractmethod
    def create(self, inp: StudentCreateInput) -> Student:
        pass

    @abstractmethod
    def update(self, student_id: ID, inp: StudentUpdateInput) -> Optional[Student]:
        pass

    @abstractmethod
    def delete(self, student_id: ID) -> None:
        pass

    @abstractmethod
    def find_all(self) -> List[Student]:
        pass

    @abstractmethod
    def find_one_by_id(self, student_id: ID) -> Optional[Student]:
        pass

    @abstractmethod
    def find_one_by_email(self, email: str) -> Optional[Student]:
        pass
