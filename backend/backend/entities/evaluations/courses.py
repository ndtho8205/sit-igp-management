from typing import Optional

from pydantic import BaseModel

from backend.entities.types import StudentYear


class SupervisorScore(BaseModel):
    daily_activities_1: float
    daily_activities_2: float
    meeting_presentation_1: float
    meeting_presentation_2: float


class LabRotation(BaseModel):
    course_score: float


class ThesisProgram(BaseModel):
    supervisor_evaluation: Optional[SupervisorScore]

    def course_score(
        self,
        student_year: StudentYear,
        semester_end_presentation_average_score: float,
        lab_rotation_score: Optional[float],
    ) -> Optional[float]:
        if self.supervisor_evaluation is None:
            return None

        tmp_score = (
            self.supervisor_evaluation.daily_activities_1 * 0.35
            + self.supervisor_evaluation.daily_activities_2 * 0.35
            + self.supervisor_evaluation.meeting_presentation_1 * 0.1
            + self.supervisor_evaluation.meeting_presentation_2 * 0.1
            + semester_end_presentation_average_score * 0.1
        )

        if student_year == StudentYear.FIRST:
            return tmp_score

        if student_year == StudentYear.SECOND:
            if lab_rotation_score is None:
                raise AttributeError("lab rotation score is required")
            return 5.0 / 6.0 * tmp_score + 1.0 / 6.0 * lab_rotation_score

        raise NotImplementedError()


class LabSeminar(BaseModel):
    supervisor_evaluation: Optional[SupervisorScore]

    def course_score(
        self,
        student_year: StudentYear,
        semester_end_presentation_average_score: float,
        lab_rotation_score: Optional[float],
    ) -> Optional[float]:
        if self.supervisor_evaluation is None:
            return None

        tmp_score = (
            self.supervisor_evaluation.daily_activities_1 * 0.35
            + self.supervisor_evaluation.daily_activities_2 * 0.15
            + self.supervisor_evaluation.meeting_presentation_1 * 0.3
            + self.supervisor_evaluation.meeting_presentation_2 * 0.1
            + semester_end_presentation_average_score * 0.1
        )

        if student_year == StudentYear.FIRST:
            return tmp_score

        if student_year == StudentYear.SECOND:
            if lab_rotation_score is None:
                raise AttributeError("lab rotation score is required")
            return 0.5 * tmp_score + 0.5 * lab_rotation_score

        raise NotImplementedError()
