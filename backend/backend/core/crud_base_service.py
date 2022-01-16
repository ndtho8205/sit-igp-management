# pylint: disable=invalid-name
from typing import List, Type, Generic, TypeVar, Optional

import sqlalchemy as sa
from pydantic.main import BaseModel
from sqlalchemy.orm.session import Session

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
        return db_session.query(self.Schema).where(self.Schema.id_ == id_).first()

    def update(
        self, db_session: Session, id_: types.ID, obj: UpdateDtoType
    ) -> SchemaType:
        stmt = (
            sa.update(self.Schema)
            .where(self.Schema.id_ == id_)
            .values(**jsonable_encoder(obj.dict(exclude_unset=True)))
            .returning(self.Schema)
        )
        orm_stmt = (
            sa.select(self.Schema)
            .from_statement(stmt)
            .execution_options(populate_existing=True)
        )

        list_db_obj: List[SchemaType] = []
        for db_obj in db_session.execute(orm_stmt).scalars():
            list_db_obj.append(db_obj)

        db_session.commit()

        for db_obj in list_db_obj:
            db_session.refresh(db_obj)

        return list_db_obj[0]

    def remove(self, db_session: Session, id_: types.ID) -> None:
        stmt = (
            sa.update(self.Schema).where(self.Schema.id_ == id_).values(is_deleted=True)
        )
        db_session.execute(stmt)
        db_session.commit()
