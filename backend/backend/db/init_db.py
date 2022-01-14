# pylint: disable=unused-import, import-outside-toplevel

from backend.db.session import engine
from backend.db.base_schema import BaseSchema


def init_db() -> None:

    # import all schemas
    from backend.api.students import StudentSchema  # noqa: F401
    from backend.api.professors import ProfessorSchema  # noqa: F401
    from backend.api.semester_end_presentations import (  # noqa: F401
        SemesterEndPresentationsSchema,
    )

    BaseSchema.metadata.create_all(bind=engine)
