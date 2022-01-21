from typing import Optional

from pydantic import BaseModel

from backend.entities.types import ID, StudentYear


class LabRotationEvaluation(BaseModel):
    presentation_id: ID
    course_score: float

    class Config:
        orm_mode = True


class ThesisProgramEvaluation(BaseModel):
    presentation_id: ID

    score_daily_activities_1: float
    score_daily_activities_2: float
    score_meeting_presentation_1: float
    score_meeting_presentation_2: float
    course_score: float

    class Config:
        orm_mode = True

    def compute_course_score(
        self,
        student_year: StudentYear,
        semester_end_presentation_average_score: float,
        lab_rotation_score: Optional[float],
    ) -> Optional[float]:
        tmp_score = (
            self.score_daily_activities_1 * 0.35
            + self.score_daily_activities_2 * 0.35
            + self.score_meeting_presentation_1 * 0.1
            + self.score_meeting_presentation_2 * 0.1
            + semester_end_presentation_average_score * 0.1
        )

        if student_year == StudentYear.FIRST:
            return tmp_score

        if student_year == StudentYear.SECOND:
            if lab_rotation_score is None:
                raise AttributeError("lab rotation score is required")
            return 5.0 / 6.0 * tmp_score + 1.0 / 6.0 * lab_rotation_score

        raise NotImplementedError()


class LabSeminarEvaluation(BaseModel):
    presentation_id: ID

    score_daily_activities_1: float
    score_daily_activities_2: float
    score_meeting_presentation_1: float
    score_meeting_presentation_2: float
    course_score: float

    class Config:
        orm_mode = True

    def compute_course_score(
        self,
        student_year: StudentYear,
        semester_end_presentation_average_score: float,
        lab_rotation_score: Optional[float],
    ) -> Optional[float]:
        tmp_score = (
            self.score_daily_activities_1 * 0.35
            + self.score_daily_activities_2 * 0.15
            + self.score_meeting_presentation_1 * 0.3
            + self.score_meeting_presentation_2 * 0.1
            + semester_end_presentation_average_score * 0.1
        )

        if student_year == StudentYear.FIRST:
            return tmp_score

        if student_year == StudentYear.SECOND:
            if lab_rotation_score is None:
                raise AttributeError("lab rotation score is required")
            return 0.5 * tmp_score + 0.5 * lab_rotation_score

        raise NotImplementedError()
