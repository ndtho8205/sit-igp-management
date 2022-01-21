from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm.session import Session

from backend.entities.types import ID
from backend.usecases.inputs import (
    LabRotationEvaluationCreateInput,
    LabRotationEvaluationUpdateInput,
)
from backend.adapters.pg.base_repository import BaseRepository
from backend.entities.evaluations.courses import LabRotationEvaluation
from backend.adapters.pg.schemas.lab_rotation_evaluation import (
    LabRotationEvaluationSchema,
)
from backend.usecases.repositories.lab_rotation_repository import LabRotationRepository


class LabRotationRepositoryAdapter(
    LabRotationRepository,
    BaseRepository[
        LabRotationEvaluationSchema,
        LabRotationEvaluationCreateInput,
        LabRotationEvaluationUpdateInput,
    ],
):
    def create(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: LabRotationEvaluationCreateInput,
    ) -> LabRotationEvaluation:
        db_evaluation = self._create(db_session, inp)
        return self.schema_to_entity(db_evaluation)

    def update(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: LabRotationEvaluationUpdateInput,
    ) -> Optional[LabRotationEvaluation]:
        db_evaluation = self.find_one_by_presentation_id(db_session, presentation_id)
        if db_evaluation is None:
            return None

        stmt = (
            sa.update(LabRotationEvaluationSchema)
            .where(
                LabRotationEvaluationSchema.presentation_id
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
    ) -> Optional[LabRotationEvaluation]:
        db_evaluation: Optional[LabRotationEvaluationSchema] = (
            db_session.query(LabRotationEvaluationSchema)
            .where(LabRotationEvaluationSchema.presentation_id == presentation_id)
            .first()
        )
        if db_evaluation is None:
            return None

        return self.schema_to_entity(db_evaluation)

    # pylint: disable=no-self-use
    def schema_to_entity(
        self,
        obj: LabRotationEvaluationSchema,
    ) -> LabRotationEvaluation:
        return LabRotationEvaluation.from_orm(obj)


lab_rotation_repository = LabRotationRepositoryAdapter(LabRotationEvaluationSchema)
