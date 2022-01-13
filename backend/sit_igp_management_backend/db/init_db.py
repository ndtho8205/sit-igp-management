# pylint: disable=unused-import, import-outside-toplevel

from sit_igp_management_backend.db.session import engine
from sit_igp_management_backend.db.base_schema import BaseSchema


def init_db() -> None:

    # import all schemas
    from sit_igp_management_backend.api.students import StudentSchema  # noqa: F401
    from sit_igp_management_backend.api.professors import ProfessorSchema  # noqa: F401
    from sit_igp_management_backend.api.semester_end_presentations import (  # noqa: F401
        SemesterEndPresentationsSchema,
    )

    BaseSchema.metadata.create_all(bind=engine)
