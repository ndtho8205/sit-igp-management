# pylint: disable=invalid-name
from typing import List, Type, Generic, TypeVar, Optional

import sqlalchemy as sa
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from backend.db import BaseSchema
from backend.core import types


SchemaType = TypeVar("SchemaType", bound=BaseSchema)
CreateDtoType = TypeVar("CreateDtoType", bound=BaseModel)
UpdateDtoType = TypeVar("UpdateDtoType", bound=BaseModel)


class CRUDBaseService(Generic[SchemaType, CreateDtoType, UpdateDtoType]):
    def __init__(self, Schema: Type[SchemaType]):  # noqa: invalid-name
        self.Schema = Schema

    def create(self, db_session: Session, obj: CreateDtoType) -> SchemaType:
        db_obj = self.Schema(**jsonable_encoder(obj))
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def find_all(self, db_session: Session) -> List[SchemaType]:
        return (
            db_session.query(self.Schema)
            .where(self.Schema.is_deleted.is_(False))
            .order_by(self.Schema.created_at.desc())
            .all()
        )

    def find_one_by_id(self, db_session: Session, id_: types.ID) -> Optional[SchemaType]:
        return db_session.query(self.Schema).get(id_)

    def update_by_id(
        self,
        db_session: Session,
        id_: types.ID,
        obj: UpdateDtoType,
    ) -> Optional[SchemaType]:
        db_obj = self.find_one_by_id(db_session, id_)
        if db_obj is None:
            return None

        stmt = (
            sa.update(self.Schema)
            .where(self.Schema.id_ == id_)
            .values(obj.dict(exclude_unset=True))
        )
        db_session.execute(stmt)
        db_session.commit()
        db_session.refresh(db_obj)

        return db_obj

    def remove_by_id(self, db_session: Session, id_: types.ID) -> None:
        stmt = (
            sa.update(self.Schema).where(self.Schema.id_ == id_).values(is_deleted=True)
        )
        db_session.execute(stmt)
        db_session.commit()
