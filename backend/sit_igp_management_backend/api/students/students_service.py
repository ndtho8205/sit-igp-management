from typing import Any

import sqlalchemy
from sqlalchemy.orm import Session

from .students_dto import CreateStudentDto, UpdateStudentDto
from .students_schema import StudentSchema


def create(
    db_session: Session,
    create_student_dto: CreateStudentDto,
) -> Any:
    db_student = StudentSchema(**create_student_dto.dict())
    db_session.add(db_student)
    db_session.commit()
    db_session.refresh(db_student)

    return db_student


def find_all(
    db_session: Session,
) -> Any:
    return db_session.query(StudentSchema).all()


def find_one_by_id(
    db_session: Session,
    student_id: int,
) -> Any:
    return (
        db_session.query(StudentSchema)
        .filter(StudentSchema.student_id == student_id)
        .first()
    )


def update(
    db_session: Session,
    student_id: int,
    update_student_dto: UpdateStudentDto,
) -> Any:
    stmt = (
        sqlalchemy.update(StudentSchema)
        .where(
            StudentSchema.student_id == student_id,
        )
        .values(**update_student_dto.dict(exclude_unset=True))
        .returning(StudentSchema)
    )
    orm_stmt = (
        sqlalchemy.select(StudentSchema)
        .from_statement(stmt)
        .execution_options(populate_existing=True)
    )

    updated_students = []
    for student in db_session.execute(orm_stmt).scalars():
        updated_students.append(student)

    db_session.commit()

    for student in updated_students:
        db_session.refresh(student)

    return updated_students


def remove(
    db_session: Session,
    student_id: int,
) -> Any:
    db_session.query(StudentSchema).filter(
        StudentSchema.student_id == student_id,
    ).delete()
    db_session.commit()
    return {
        "student_id": student_id,
    }
