from typing import Optional

from sqlalchemy.orm.session import Session

from backend.core.crud_base_service import CRUDBaseService
from backend.api.professors.professors_dto import ProfessorCreateDto, ProfessorUpdateDto
from backend.api.professors.professors_schema import ProfessorSchema


class ProfessorsService(
    CRUDBaseService[ProfessorSchema, ProfessorCreateDto, ProfessorUpdateDto],
):
    def find_one_by_email(
        self,
        db_session: Session,
        email: str,
    ) -> Optional[ProfessorSchema]:
        return db_session.query(self.Schema).filter(self.Schema.email == email).first()

    def is_exists(
        self,
        db_session: Session,
        professor_id: Optional[int],
    ) -> bool:
        if professor_id is None:
            return True

        db_professor = self.find_one_by_id(db_session, professor_id)
        if db_professor:
            return True

        return False


service = ProfessorsService(ProfessorSchema)
