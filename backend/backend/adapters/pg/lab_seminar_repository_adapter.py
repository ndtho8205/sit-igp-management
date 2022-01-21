from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm.session import Session

from backend.entities.types import ID
from backend.usecases.inputs import (
    LabSeminarEvaluationCreateInput,
    LabSeminarEvaluationUpdateInput,
)
from backend.adapters.pg.base_repository import BaseRepository
from backend.entities.evaluations.courses import LabSeminarEvaluation
from backend.adapters.pg.schemas.lab_seminar_evaluation import (
    LabSeminarEvaluationSchema,
)
from backend.usecases.repositories.lab_seminar_repository import LabSeminarRepository


class LabSeminarRepositoryAdapter(
    LabSeminarRepository,
    BaseRepository[
        LabSeminarEvaluationSchema,
        LabSeminarEvaluationCreateInput,
        LabSeminarEvaluationUpdateInput,
    ],
):
    def create(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: LabSeminarEvaluationCreateInput,
    ) -> LabSeminarEvaluation:
        db_evaluation = self._create(db_session, inp)
        return self.schema_to_entity(db_evaluation)

    def update(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: LabSeminarEvaluationUpdateInput,
    ) -> Optional[LabSeminarEvaluation]:
        db_evaluation = self.find_one_by_presentation_id(db_session, presentation_id)
        if db_evaluation is None:
            return None

        stmt = (
            sa.update(LabSeminarEvaluationSchema)
            .where(
                LabSeminarEvaluationSchema.presentation_id
                == db_evaluation.presentation_id
            )
            .values(inp.dict(exclude_unset=True))
        )
        db_session.execute(stmt)
        db_session.commit()

        db_evaluation = self.find_one_by_presentation_id(
            db_session,
            presentation_id,
        )

        return db_evaluation

    def find_one_by_presentation_id(
        self, db_session: Session, presentation_id: ID
    ) -> Optional[LabSeminarEvaluation]:
        db_evaluation: Optional[LabSeminarEvaluationSchema] = (
            db_session.query(LabSeminarEvaluationSchema)
            .where(LabSeminarEvaluationSchema.presentation_id == presentation_id)
            .first()
        )
        if db_evaluation is None:
            return None

        return self.schema_to_entity(db_evaluation)

    # pylint: disable=no-self-use
    def schema_to_entity(
        self,
        obj: LabSeminarEvaluationSchema,
    ) -> LabSeminarEvaluation:
        return LabSeminarEvaluation.from_orm(obj)


lab_seminar_repository = LabSeminarRepositoryAdapter(
    LabSeminarEvaluationSchema
)
