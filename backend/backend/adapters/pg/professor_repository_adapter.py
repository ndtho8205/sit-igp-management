from typing import List, Optional

from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.inputs import ProfessorCreateInput, ProfessorUpdateInput
from backend.usecases.repositories import ProfessorRepository
from backend.adapters.pg.base_repository import BaseRepository
from backend.adapters.pg.schemas.professor import ProfessorSchema


class ProfessorRepositoryAdapter(
    ProfessorRepository,
    BaseRepository[
        ProfessorSchema,
        ProfessorCreateInput,
        ProfessorUpdateInput,
    ],
):
    def create(self, db_session: Session, inp: ProfessorCreateInput) -> Professor:
        db_professor = self._create(db_session, inp)
        return self.schema_to_entity(db_professor)

    def update(
        self,
        db_session: Session,
        professor_id: ID,
        inp: ProfessorUpdateInput,
    ) -> Optional[Professor]:
        db_professor = self._update(db_session, professor_id, inp)
        if db_professor is None:
            return None
        return self.schema_to_entity(db_professor)

    def delete(self, db_session: Session, professor_id: ID) -> None:
        self._delete(db_session, professor_id)

    def find_all(self, db_session: Session) -> List[Professor]:
        db_professors = self._find_all(db_session)
        return [self.schema_to_entity(db_professor) for db_professor in db_professors]

    def find_one_by_id(
        self,
        db_session: Session,
        professor_id: ID,
    ) -> Optional[Professor]:
        db_professor = self._find_one_by_id(db_session, professor_id)
        if db_professor is None:
            return None
        return self.schema_to_entity(db_professor)

    def find_one_by_email(self, db_session: Session, email: str) -> Optional[Professor]:
        db_professor = (
            db_session.query(self.Schema).where(self.Schema.email == email).first()
        )

        if db_professor is None:
            return None

        return self.schema_to_entity(db_professor)

    # pylint: disable=no-self-use
    def schema_to_entity(self, obj: ProfessorSchema) -> Professor:
        return Professor.from_orm(obj)


professor_repository = ProfessorRepositoryAdapter(ProfessorSchema)
