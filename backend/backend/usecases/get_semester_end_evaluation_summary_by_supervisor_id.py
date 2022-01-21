from typing import List

from sqlalchemy.orm.session import Session

from backend.entities import Professor
from backend.entities.types import ID
from backend.usecases.repositories import (
    LabSeminarRepository,
    LabRotationRepository,
    PresentationRepository,
    ThesisProgramRepository,
)
from backend.entities.semester_end_evaluation import SemesterEndEvaluation


def get_semester_end_evaluation_summary_by_supervisor_id(
    supervisor_id: ID,
    current_user: Professor,
    presentation_repository: PresentationRepository,
    thesis_program_repository: ThesisProgramRepository,
    lab_seminar_repository: LabSeminarRepository,
    lab_rotation_repository: LabRotationRepository,
    db_session: Session,
) -> List[SemesterEndEvaluation]:
    list_semester_end_evaluation = []

    presentations = presentation_repository.find_all(db_session)

    for presentation in presentations:
        student = presentation.student

        list_supervisor_id = []
        if student.supervisor is not None:
            list_supervisor_id.append(student.supervisor.id_)
        if student.advisor1 is not None:
            list_supervisor_id.append(student.advisor1.id_)

        if supervisor_id not in list_supervisor_id:
            continue

        presentation_id = presentation.id_

        list_semester_end_evaluation.append(
            SemesterEndEvaluation(
                presentation=presentation,
                thesis_program=thesis_program_repository.find_one_by_presentation_id(
                    db_session, presentation_id
                ),
                lab_seminar=lab_seminar_repository.find_one_by_presentation_id(
                    db_session, presentation_id
                ),
                lab_rotation=lab_rotation_repository.find_one_by_presentation_id(
                    db_session, presentation_id
                ),
            )
        )

    return list_semester_end_evaluation
