from typing import Optional

from sqlalchemy.orm.session import Session

from backend.core.crud_base_service import CRUDBaseService
from backend.api.students.students_dto import StudentCreateDto, StudentUpdateDto
from backend.api.students.students_schema import StudentSchema


class StudentsService(CRUDBaseService[StudentSchema, StudentCreateDto, StudentUpdateDto]):
    def find_one_by_email(
        self,
        db_session: Session,
        email: str,
    ) -> Optional[StudentSchema]:
        return db_session.query(self.Schema).where(self.Schema.email == email).first()

    def is_email_unique(self, db_session: Session, email: str) -> bool:
        return self.find_one_by_email(db_session, email) is None


service = StudentsService(StudentSchema)
