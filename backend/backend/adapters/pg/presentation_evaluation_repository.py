from typing import List, Optional

import sqlalchemy as sa
from sqlalchemy.orm.session import Session

from fastapi.encoders import jsonable_encoder

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


class PresentationEvaluationRepositoryAdapter(PresentationEvaluationRepository):
    db_session: Session

    def set_session(self, db_session: Session) -> None:
        self.db_session = db_session

    def __init__(self) -> None:
        self.repository = BaseRepository[
            PresentationEvaluationSchema,
            PresentationEvaluationCreateInput,
            PresentationEvaluationUpdateInput,
        ](PresentationEvaluationSchema)

    def create(
        self,
        inp: PresentationEvaluationCreateInput,
        question_score: float,
    ) -> PresentationEvaluation:
        db_evaluation: PresentationEvaluationSchema = PresentationEvaluationSchema(
            **jsonable_encoder(inp),
            question_score=question_score,
        )
        self.db_session.add(db_evaluation)
        self.db_session.commit()
        self.db_session.refresh(db_evaluation)
        return self.schema_to_entity(db_evaluation)

    def update_by_presentation_and_reviewer_id(
        self,
        presentation_id: ID,
        reviewer_id: ID,
        inp: PresentationEvaluationUpdateInput,
        question_score: float,
    ) -> Optional[PresentationEvaluation]:
        db_evaluation = self.find_one_by_presentation_and_reviewer_id(
            presentation_id, reviewer_id
        )
        if db_evaluation is None:
            return None

        stmt = (
            sa.update(PresentationEvaluationSchema)
            .where(PresentationEvaluationSchema.id_ == db_evaluation.id_)
            .values(inp.dict(exclude_unset=True), question_score=question_score)
        )
        self.db_session.execute(stmt)
        self.db_session.commit()
        self.db_session.refresh(db_evaluation)

        db_evaluation = self.find_one_by_presentation_and_reviewer_id(
            presentation_id, reviewer_id
        )

        return db_evaluation

    def delete(self, evaluation_id: ID) -> None:
        self.repository.delete(self.db_session, evaluation_id)

    def find_all(
        self,
        reviewer_id: Optional[ID],
    ) -> List[PresentationEvaluation]:
        if reviewer_id is None:
            db_evaluations = self.repository.find_all(self.db_session)
        else:
            db_evaluations = (
                self.db_session.query(PresentationEvaluationSchema)
                .where(
                    PresentationEvaluationSchema.reviewer_id == reviewer_id,
                )
                .where(PresentationEvaluationSchema.is_deleted.is_(False))
                .order_by(PresentationEvaluationSchema.created_at.desc())
                .all()
            )

        return [self.schema_to_entity(db_evaluation) for db_evaluation in db_evaluations]

    def find_one_by_id(self, presentation_id: ID) -> Optional[PresentationEvaluation]:
        db_evaluation = self.repository.find_one_by_id(self.db_session, presentation_id)
        if db_evaluation is None:
            return None
        return self.schema_to_entity(db_evaluation)

    def find_one_by_presentation_and_reviewer_id(
        self, presentation_id: ID, reviewer_id: ID
    ) -> Optional[PresentationEvaluation]:
        db_evaluation = (
            self.db_session.query(PresentationEvaluationSchema)
            .where(
                PresentationEvaluationSchema.presentation_id == presentation_id,
                PresentationEvaluationSchema.reviewer_id == reviewer_id,
            )
            .first()
        )
        return db_evaluation

    # pylint: disable=no-self-use
    def schema_to_entity(
        self,
        obj: PresentationEvaluationSchema,
    ) -> PresentationEvaluation:
        return PresentationEvaluation.from_orm(obj)


presentation_evaluation_repository = PresentationEvaluationRepositoryAdapter()
