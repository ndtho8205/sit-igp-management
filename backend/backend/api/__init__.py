# pylint: disable=unused-import,import-outside-toplevel
# flake8: noqa


def import_all_schemas() -> None:
    from backend.api.students import StudentSchema
    from backend.api.professors import ProfessorSchema
    from backend.api.presentations import PresentationSchema
    from backend.api.presentation_evaluations import PresentationEvaluationSchema
