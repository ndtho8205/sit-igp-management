from typing import List, Optional

import sqlalchemy as sa
from sqlalchemy.orm.session import Session

from backend.entities import PresentationEvaluation
from backend.entities.types import ID
from backend.usecases.inputs import (
    PresentationEvaluationCreateInput,
    PresentationEvaluationUpdateInput,
)
from backend.usecases.repositories import PresentationEvaluationRepository
from backend.adapters.pg.base_repository import BaseRepository
from backend.adapters.pg.schemas.presentation_evaluation import (
    PresentationEvaluationSchema,
)


class PresentationEvaluationRepositoryAdapter(
    PresentationEvaluationRepository,
    BaseRepository[
        PresentationEvaluationSchema,
        PresentationEvaluationCreateInput,
        PresentationEvaluationUpdateInput,
    ],
):
    def create(
        self,
        db_session: Session,
        presentation_id: ID,
        reviewer_id: ID,
        inp: PresentationEvaluationCreateInput,
    ) -> PresentationEvaluation:
        db_evaluation = self._create(db_session, inp)
        return self.schema_to_entity(db_evaluation)

    def update(
        self,
        db_session: Session,
        presentation_id: ID,
        reviewer_id: ID,
        inp: PresentationEvaluationUpdateInput,
    ) -> Optional[PresentationEvaluation]:
        db_evaluation = self.find_one_by_presentation_and_reviewer_id(
            db_session,
            presentation_id,
            reviewer_id,
        )
        if db_evaluation is None:
            return None

        stmt = (
            sa.update(PresentationEvaluationSchema)
            .where(PresentationEvaluationSchema.id_ == db_evaluation.id_)
            .values(inp.dict(exclude_unset=True))
        )
        db_session.execute(stmt)
        db_session.commit()
        db_session.refresh(db_evaluation)

        db_evaluation = self.find_one_by_presentation_and_reviewer_id(
            db_session,
            presentation_id,
            reviewer_id,
        )

        return db_evaluation

    def find_all(
        self,
        db_session: Session,
        reviewer_id: Optional[ID],
    ) -> List[PresentationEvaluation]:
        if reviewer_id is None:
            db_evaluations = self._find_all(db_session)
        else:
            db_evaluations = (
                db_session.query(PresentationEvaluationSchema)
                .where(
                    PresentationEvaluationSchema.reviewer_id == reviewer_id,
                )
                .where(PresentationEvaluationSchema.is_deleted.is_(False))
                .order_by(PresentationEvaluationSchema.created_at.desc())
                .all()
            )

        return [self.schema_to_entity(db_evaluation) for db_evaluation in db_evaluations]

    def find_one_by_presentation_and_reviewer_id(
        self,
        db_session: Session,
        presentation_id: ID,
        reviewer_id: ID,
    ) -> Optional[PresentationEvaluation]:
        db_evaluation: Optional[PresentationEvaluationSchema] = (
            db_session.query(PresentationEvaluationSchema)
            .where(
                PresentationEvaluationSchema.presentation_id == presentation_id,
                PresentationEvaluationSchema.reviewer_id == reviewer_id,
            )
            .first()
        )
        if db_evaluation is None:
            return None

        return self.schema_to_entity(db_evaluation)

    # pylint: disable=no-self-use
    def schema_to_entity(
        self,
        obj: PresentationEvaluationSchema,
    ) -> PresentationEvaluation:
        return PresentationEvaluation.from_orm(obj)


presentation_evaluation_repository = PresentationEvaluationRepositoryAdapter(
    PresentationEvaluationSchema
)
