from typing import List, Optional

from abc import ABC, abstractmethod

from backend.entities.types import ID
from backend.usecases.inputs import PresentationCreateInput, PresentationUpdateInput
from backend.entities.evaluations.presentation import Presentation


class PresentationRepository(ABC):
    @abstractmethod
    def create(self, inp: PresentationCreateInput) -> Presentation:
        pass

    @abstractmethod
    def update(
        self,
        presentation_id: ID,
        inp: PresentationUpdateInput,
    ) -> Optional[Presentation]:
        pass

    @abstractmethod
    def delete(self, presentation_id: ID) -> None:
        pass

    @abstractmethod
    def find_all(self, reviewer_id: Optional[ID]) -> List[Presentation]:
        pass

    @abstractmethod
    def find_one_by_id(self, presentation_id: ID) -> Optional[Presentation]:
        pass
