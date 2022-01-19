from typing import List, Optional

from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.usecases.inputs import ProfessorCreateInput, ProfessorUpdateInput
from backend.usecases.validators import ID
from backend.usecases.repositories import ProfessorRepository
from backend.adapters.pg.base_repository import BaseRepository
from backend.adapters.pg.schemas.professor import ProfessorSchema


class ProfessorRepositoryAdapter(ProfessorRepository):
    db_session: Session

    def set_session(self, db_session: Session) -> None:
        self.db_session = db_session

    def __init__(self) -> None:
        self.repository = BaseRepository[
            ProfessorSchema,
            ProfessorCreateInput,
            ProfessorUpdateInput,
        ](ProfessorSchema)

    def create(self, inp: ProfessorCreateInput) -> Professor:
        db_professor = self.repository.create(self.db_session, inp)
        return self.schema_to_entity(db_professor)

    def update(self, professor_id: ID, inp: ProfessorUpdateInput) -> Optional[Professor]:
        db_professor = self.repository.update(self.db_session, professor_id, inp)
        if db_professor is None:
            return None
        return self.schema_to_entity(db_professor)

    def delete(self, professor_id: ID) -> None:
        self.repository.delete(self.db_session, professor_id)

    def find_all(self) -> List[Professor]:
        db_professors = self.repository.find_all(self.db_session)
        return [self.schema_to_entity(db_professor) for db_professor in db_professors]

    def find_one_by_id(self, professor_id: ID) -> Optional[Professor]:
        db_professor = self.repository.find_one_by_id(self.db_session, professor_id)
        if db_professor is None:
            return None
        return self.schema_to_entity(db_professor)

    def find_one_by_email(self, email: str) -> Optional[Professor]:
        db_professor = (
            self.db_session.query(self.repository.Schema)
            .where(self.repository.Schema.email == email)
            .first()
        )

        if db_professor is None:
            return None

        return self.schema_to_entity(db_professor)

    # pylint: disable=no-self-use
    def schema_to_entity(self, obj: ProfessorSchema) -> Professor:
        return Professor.from_orm(obj)


professor_repository = ProfessorRepositoryAdapter()
