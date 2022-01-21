from typing import List, Optional

from sqlalchemy.orm.session import Session

from backend.entities import Student
from backend.entities.types import ID
from backend.usecases.inputs import StudentCreateInput, StudentUpdateInput
from backend.usecases.repositories import StudentRepository
from backend.adapters.pg.base_repository import BaseRepository
from backend.adapters.pg.schemas.student import StudentSchema
from backend.adapters.pg.professor_repository_adapter import professor_repository


class StudentRepositoryAdapter(
    StudentRepository,
    BaseRepository[
        StudentSchema,
        StudentCreateInput,
        StudentUpdateInput,
    ],
):
    def create(self, db_session: Session, inp: StudentCreateInput) -> Student:
        db_student = self._create(db_session, inp)
        return self.schema_to_entity(db_session, db_student)

    def update(
        self,
        db_session: Session,
        student_id: ID,
        inp: StudentUpdateInput,
    ) -> Optional[Student]:
        db_student = self._update(db_session, student_id, inp)
        if db_student is None:
            return None
        return self.schema_to_entity(db_session, db_student)

    def delete(self, db_session: Session, student_id: ID) -> None:
        self._delete(db_session, student_id)

    def find_all(
        self,
        db_session: Session,
    ) -> List[Student]:
        db_students = self._find_all(db_session)
        return [
            self.schema_to_entity(db_session, db_student) for db_student in db_students
        ]

    def find_one_by_id(self, db_session: Session, student_id: ID) -> Optional[Student]:
        db_student = self._find_one_by_id(db_session, student_id)
        if db_student is None:
            return None
        return self.schema_to_entity(db_session, db_student)

    def find_one_by_email(self, db_session: Session, email: str) -> Optional[Student]:
        db_student = (
            db_session.query(self.Schema).where(self.Schema.email == email).first()
        )

        if db_student is None:
            return None

        return self.schema_to_entity(db_session, db_student)

    # pylint: disable=no-self-use
    def schema_to_entity(self, db_session: Session, obj: StudentSchema) -> Student:
        student = Student.from_orm(obj)

        if obj.supervisor_id is not None:
            student.supervisor = professor_repository.find_one_by_id(
                db_session,
                obj.supervisor_id,
            )

        if obj.advisor1_id is not None:
            student.advisor1 = professor_repository.find_one_by_id(
                db_session,
                obj.advisor1_id,
            )

        if obj.advisor2_id is not None:
            student.advisor2 = professor_repository.find_one_by_id(
                db_session,
                obj.advisor2_id,
            )

        return student


student_repository = StudentRepositoryAdapter(StudentSchema)
