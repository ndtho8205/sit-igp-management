from sqlalchemy.orm.session import Session

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import api
from backend.db.session import DbSession
from backend.configs.envs.base import BaseAppConfig
from backend.api.professors.professors_schema import ProfessorSchema
from backend.api.professors.professors_service import service as professors_service


def init_app(config: BaseAppConfig) -> FastAPI:
    _init_db(config, DbSession())

    app = FastAPI(
        title=config.APP_NAME,
        openapi_url=f"{config.API_PREFIX}/openapi.json",
    )

    if config.CORS_ALLOW_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=config.CORS_ALLOW_ORIGINS,
            allow_credentials=True,
            allow_methods=["HEAD", "GET", "POST", "PUT", "DELETE"],
            allow_headers=["*"],
        )

    app.include_router(api.router, prefix=config.API_PREFIX)

    return app


def _init_db(config: BaseAppConfig, db_session: Session) -> None:
    superuser = professors_service.find_one_by_email(db_session, config.SUPERUSER_EMAIL)
    if not superuser:
        db_superuser = ProfessorSchema(
            full_name=config.SUPERUSER_FULLNAME,
            email=config.SUPERUSER_EMAIL,
            is_superuser=True,
        )
        db_session.add(db_superuser)
        db_session.commit()
