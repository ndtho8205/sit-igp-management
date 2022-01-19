from typing import List, Optional

from abc import ABC, abstractmethod

from backend.entities import Professor
from backend.usecases.inputs import ProfessorCreateInput, ProfessorUpdateInput
from backend.usecases.validators import ID


class ProfessorRepository(ABC):
    @abstractmethod
    def create(self, inp: ProfessorCreateInput) -> Professor:
        pass

    @abstractmethod
    def update(self, professor_id: ID, inp: ProfessorUpdateInput) -> Optional[Professor]:
        pass

    @abstractmethod
    def delete(self, professor_id: ID) -> None:
        pass

    @abstractmethod
    def find_all(self) -> List[Professor]:
        pass

    @abstractmethod
    def find_one_by_id(self, professor_id: ID) -> Optional[Professor]:
        pass

    @abstractmethod
    def find_one_by_email(self, email: str) -> Optional[Professor]:
        pass
