from typing import List, Optional

from sqlalchemy.orm.session import Session

from backend.core import types
from backend.core.crud_base_service import CRUDBaseService
from backend.api.presentation_evaluations.presentation_evaluations_dto import (
    PresentationEvaluationCreateDto,
    PresentationEvaluationUpdateDto,
)
from backend.api.presentation_evaluations.presentation_evaluations_schema import (
    PresentationEvaluationSchema,
)


class PresentationEvaluationsService(
    CRUDBaseService[
        PresentationEvaluationSchema,
        PresentationEvaluationCreateDto,
        PresentationEvaluationUpdateDto,
    ],
):
    def find_all_evaluations_per_presentation(
        self,
        db_session: Session,
        presentation_id: types.ID,
    ) -> List[PresentationEvaluationSchema]:
        return (
            db_session.query(self.Schema)
            .where(
                self.Schema.presentation_id == presentation_id,
                self.Schema.is_deleted.is_(False),
            )
            .order_by(self.Schema.created_at.desc())
            .all()
        )

    def find_one_by_presentation_and_reviewer_id(
        self,
        db_session: Session,
        presentation_id: types.ID,
        reviewer_id: types.ID,
    ) -> Optional[PresentationEvaluationSchema]:
        return (
            db_session.query(self.Schema)
            .where(
                self.Schema.presentation_id == presentation_id,
                self.Schema.reviewer_id == reviewer_id,
            )
            .first()
        )


service = PresentationEvaluationsService(PresentationEvaluationSchema)
