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
        return db_session.query(self.Schema).filter(self.Schema.email == email).first()

    def is_exists(
        self,
        db_session: Session,
        student_id: int,
    ) -> bool:
        db_student = self.find_one_by_id(db_session, student_id)
        if db_student:
            return True

        return False


service = StudentsService(StudentSchema)
