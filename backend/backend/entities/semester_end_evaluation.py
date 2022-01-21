from typing import Optional

from pydantic.main import BaseModel

from backend.entities.evaluations.courses import (
    LabSeminarEvaluation,
    LabRotationEvaluation,
    ThesisProgramEvaluation,
)
from backend.entities.evaluations.presentation import Presentation


class SemesterEndEvaluation(BaseModel):
    presentation: Presentation
    thesis_program: Optional[ThesisProgramEvaluation]
    lab_seminar: Optional[LabSeminarEvaluation]
    lab_rotation: Optional[LabRotationEvaluation]
