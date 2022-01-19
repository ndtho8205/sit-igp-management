from typing import List, Type, Generic, TypeVar, Optional

import sqlalchemy as sa
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from backend.adapters.pg.schemas import BaseSchema
from backend.usecases.validators import ID


SchemaType = TypeVar("SchemaType", bound=BaseSchema)
CreateInputType = TypeVar("CreateInputType", bound=BaseModel)
UpdateInputType = TypeVar("UpdateInputType", bound=BaseModel)


class BaseRepository(Generic[SchemaType, CreateInputType, UpdateInputType]):
    def __init__(
        self,
        Schema: Type[SchemaType],  # pylint: disable=invalid-name # noqa: N803
    ):
        self.Schema = Schema  # pylint: disable=invalid-name

    def create(self, db_session: Session, inp: CreateInputType) -> SchemaType:
        db_obj: SchemaType = self.Schema(**jsonable_encoder(inp))
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def update(
        self,
        db_session: Session,
        id_: ID,
        inp: UpdateInputType,
    ) -> Optional[SchemaType]:
        db_obj = self.find_one_by_id(db_session, id_)
        if db_obj is None:
            return None

        stmt = (
            sa.update(self.Schema)
            .where(self.Schema.id_ == id_)
            .values(inp.dict(exclude_unset=True))
        )
        db_session.execute(stmt)
        db_session.commit()
        db_session.refresh(db_obj)

        return db_obj

    def delete(self, db_session: Session, id_: ID) -> None:
        stmt = (
            sa.update(self.Schema).where(self.Schema.id_ == id_).values(is_deleted=True)
        )
        db_session.execute(stmt)
        db_session.commit()

    def find_all(self, db_session: Session) -> List[SchemaType]:
        return (
            db_session.query(self.Schema)
            .where(self.Schema.is_deleted.is_(False))
            .order_by(self.Schema.created_at.desc())
            .all()
        )

    def find_one_by_id(self, db_session: Session, id_: ID) -> Optional[SchemaType]:
        return db_session.query(self.Schema).get(id_)
