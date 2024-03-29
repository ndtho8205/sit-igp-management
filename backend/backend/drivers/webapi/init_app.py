# pylint: disable=unused-argument
import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

from backend.adapters.pg import professor_repository
from backend.configs import app_config
from backend.drivers.pg.session import DbSession
from backend.drivers.webapi import api
from backend.usecases.errors import (
    BadRequestError,
    ConflictError,
    ForbiddenError,
    NotFoundError,
)
from backend.usecases.inputs import ProfessorCreateInput

# Database
db_session = DbSession()
try:
    superuser = professor_repository.find_one_by_email(
        db_session, app_config.SUPERUSER_EMAIL
    )
    if superuser is None:
        professor_repository.create(
            db_session,
            ProfessorCreateInput(
                full_name=app_config.SUPERUSER_FULLNAME,
                email=app_config.SUPERUSER_EMAIL,
                is_verified=True,
                is_superuser=True,
            ),
        )
finally:
    db_session.close()


app = FastAPI(
    title=app_config.APP_NAME,
    openapi_url=f"{app_config.API_PREFIX}/openapi.json",
)


# Sentry

sentry_sdk.init(
    dsn=app_config.SENTRY_DSN,
    environment=str(app_config.APP_ENV),
    attach_stacktrace=True,
    send_default_pii=True,
    request_bodies="always",
    integrations=[SqlalchemyIntegration()],
)

try:
    app.add_middleware(SentryAsgiMiddleware)
except Exception as ex:  # pylint: disable=broad-except
    print(ex)

# Security

if app_config.CORS_ALLOW_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[app_config.CORS_ALLOW_ORIGINS],
        allow_credentials=True,
        allow_methods=["HEAD", "GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )

# Exception handlers


@app.exception_handler(ConflictError)
async def conflict_exception_handler(
    request: Request,
    exc: ConflictError,
) -> JSONResponse:
    return JSONResponse(
        status_code=409,
        content={"detail": exc.args[0]},
    )


@app.exception_handler(NotFoundError)
async def not_found_exception_handler(
    request: Request,
    exc: NotFoundError,
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"detail": exc.args[0]},
    )


@app.exception_handler(ForbiddenError)
async def forbidden_exception_handler(
    request: Request,
    exc: ForbiddenError,
) -> JSONResponse:
    return JSONResponse(
        status_code=403,
        content={"detail": "You do not have enough access privileges"},
    )


@app.exception_handler(BadRequestError)
async def bad_request_exception_handler(
    request: Request,
    exc: BadRequestError,
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": exc.args[0]},
    )


# Routers
app.include_router(api.router, prefix=app_config.API_PREFIX)
