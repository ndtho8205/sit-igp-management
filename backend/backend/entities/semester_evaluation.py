from pydantic import BaseModel

from backend.entities.evaluations.courses import LabSeminar, ThesisProgram
from backend.entities.evaluations.presentation import SemesterEndPresentation


class SemesterEvaluation(BaseModel):
    presentation: SemesterEndPresentation
    thesis_program: ThesisProgram
    lab_seminar: LabSeminar
