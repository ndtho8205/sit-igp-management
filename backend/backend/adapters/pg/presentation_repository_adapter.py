from typing import List, Optional

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.elements import or_

from backend.entities import Presentation
from backend.entities.types import ID
from backend.usecases.errors import NotFoundError
from backend.usecases.inputs import PresentationCreateInput, PresentationUpdateInput
from backend.usecases.repositories import PresentationRepository
from backend.adapters.pg.base_repository import BaseRepository
from backend.adapters.pg.schemas.presentation import PresentationSchema
from backend.adapters.pg.student_repository_adapter import student_repository
from backend.adapters.pg.professor_repository_adapter import professor_repository
from backend.adapters.pg.presentation_evaluation_repository_adapter import (
    presentation_evaluation_repository,
)


class PresentationRepositoryAdapter(
    PresentationRepository,
    BaseRepository[
        PresentationSchema,
        PresentationCreateInput,
        PresentationUpdateInput,
    ],
):
    def create(self, db_session: Session, inp: PresentationCreateInput) -> Presentation:
        db_presentation = self._create(db_session, inp)
        return self.schema_to_entity(db_session, db_presentation)

    def update(
        self,
        db_session: Session,
        presentation_id: ID,
        inp: PresentationUpdateInput,
    ) -> Optional[Presentation]:
        db_presentation = self._update(db_session, presentation_id, inp)
        if db_presentation is None:
            return None
        return self.schema_to_entity(db_session, db_presentation)

    def delete(self, db_session: Session, presentation_id: ID) -> None:
        self._delete(db_session, presentation_id)

    def find_all(
        self,
        db_session: Session,
        reviewer_id: Optional[ID]=None,
    ) -> List[Presentation]:
        if reviewer_id is None:
            db_presentations = self._find_all(db_session)
        else:
            db_presentations = (
                db_session.query(PresentationSchema)
                .where(
                    or_(
                        PresentationSchema.reviewer1_id == reviewer_id,
                        PresentationSchema.reviewer2_id == reviewer_id,
                        PresentationSchema.reviewer3_id == reviewer_id,
                        PresentationSchema.reviewer4_id == reviewer_id,
                    )
                )
                .where(PresentationSchema.is_deleted.is_(False))
                .order_by(PresentationSchema.created_at.desc())
                .all()
            )

        return [
            self.schema_to_entity(db_session, db_presentation)
            for db_presentation in db_presentations
        ]

    def find_one_by_id(
        self,
        db_session: Session,
        presentation_id: ID,
    ) -> Optional[Presentation]:
        db_presentation = self._find_one_by_id(db_session, presentation_id)
        if db_presentation is None:
            return None
        return self.schema_to_entity(db_session, db_presentation)

    # pylint: disable=no-self-use
    def schema_to_entity(
        self,
        db_session: Session,
        obj: PresentationSchema,
    ) -> Presentation:
        presenter = student_repository.find_one_by_id(db_session, obj.student_id)
        if presenter is None:
            raise NotFoundError("presenter was not found")

        presentation = Presentation(
            id_=obj.id_,
            student=presenter,
            presentation_date=obj.presentation_date,
            presentation_length=obj.presentation_length,
        )

        if obj.session_chair_id is not None:
            presentation.session_chair = professor_repository.find_one_by_id(
                db_session,
                obj.session_chair_id,
            )

        if obj.reviewer1_id is not None:
            presentation.reviewer1 = professor_repository.find_one_by_id(
                db_session, obj.reviewer1_id
            )
            presentation.reviewer1_evaluation = presentation_evaluation_repository.find_one_by_presentation_and_reviewer_id(
                db_session, presentation.id_, obj.reviewer1_id
            )

        if obj.reviewer2_id is not None:
            presentation.reviewer2 = professor_repository.find_one_by_id(
                db_session, obj.reviewer2_id
            )

            presentation.reviewer2_evaluation = presentation_evaluation_repository.find_one_by_presentation_and_reviewer_id(
                db_session,
                presentation.id_,
                obj.reviewer2_id,
            )

        if obj.reviewer3_id is not None:
            presentation.reviewer3 = professor_repository.find_one_by_id(
                db_session, obj.reviewer3_id
            )

            presentation.reviewer3_evaluation = presentation_evaluation_repository.find_one_by_presentation_and_reviewer_id(
                db_session,
                presentation.id_,
                obj.reviewer3_id,
            )

        if obj.reviewer4_id is not None:
            presentation.reviewer4 = professor_repository.find_one_by_id(
                db_session, obj.reviewer4_id
            )

            presentation.reviewer4_evaluation = presentation_evaluation_repository.find_one_by_presentation_and_reviewer_id(
                db_session,
                presentation.id_,
                obj.reviewer4_id,
            )

        return presentation


presentation_repository = PresentationRepositoryAdapter(PresentationSchema)
