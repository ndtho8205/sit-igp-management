# pylint: disable=unused-import

from sit_igp_management_backend.api.students.students_schema import (  # noqa: F401
    StudentSchema,
)
from sit_igp_management_backend.api.professors.professors_schema import (  # noqa: F401
    ProfessorSchema,
)

from .session import engine
from .base_schema import BaseSchema


def init_db() -> None:
    BaseSchema.metadata.create_all(bind=engine)
