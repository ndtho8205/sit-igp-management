from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm.session import Session

from backend.entities.types import ID
from backend.usecases.inputs import (
    ThesisProgramEvaluationCreateInput,
    ThesisProgramEvaluationUpdateInput,
)
from backend.adapters.pg.base_repository import BaseRepository
from backend.entities.evaluations.courses import ThesisProgramEvaluation
from backend.adapters.pg.schemas.thesis_program_evaluation import (
    ThesisProgramEvaluationSchema,
)
from backend.usecases.repositories.thesis_program_repository import (
    ThesisProgramRepository,
)


class ThesisProgramRepositoryAdapter(
    ThesisProgramRepository,
    BaseRepository[
        ThesisProgramEvaluationSchema,
        ThesisProgramEvaluationCreateInput,
        ThesisProgramEvaluationUpdateInput,
    ],
):
    def create(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: ThesisProgramEvaluationCreateInput,
    ) -> ThesisProgramEvaluation:
        db_evaluation = self._create(db_session, inp)
        return self.schema_to_entity(db_evaluation)

    def update(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: ThesisProgramEvaluationUpdateInput,
    ) -> Optional[ThesisProgramEvaluation]:
        db_evaluation = self.find_one_by_presentation_id(db_session, presentation_id)
        if db_evaluation is None:
            return None

        stmt = (
            sa.update(ThesisProgramEvaluationSchema)
            .where(
                ThesisProgramEvaluationSchema.presentation_id
                == db_evaluation.presentation_id
            )
            .values(inp.dict(exclude_unset=True))
        )
        db_session.execute(stmt)
        db_session.commit()
        db_session.refresh(db_evaluation)

        db_evaluation = self.find_one_by_presentation_id(
            db_session,
            presentation_id,
        )

        return db_evaluation

    def find_one_by_presentation_id(
        self, db_session: Session, presentation_id: ID
    ) -> Optional[ThesisProgramEvaluation]:
        db_evaluation: Optional[ThesisProgramEvaluationSchema] = (
            db_session.query(ThesisProgramEvaluationSchema)
            .where(ThesisProgramEvaluationSchema.presentation_id == presentation_id)
            .first()
        )
        if db_evaluation is None:
            return None

        return self.schema_to_entity(db_evaluation)

    # pylint: disable=no-self-use
    def schema_to_entity(
        self,
        obj: ThesisProgramEvaluationSchema,
    ) -> ThesisProgramEvaluation:
        return ThesisProgramEvaluation.from_orm(obj)


thesis_program_repository = ThesisProgramRepositoryAdapter(ThesisProgramEvaluationSchema)
