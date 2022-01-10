from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sit_igp_management_backend.db.init_db import init_db
from sit_igp_management_backend.core.config import config
from sit_igp_management_backend.api.professors import professors_router


init_db()

app = FastAPI(
    title=config.APP_NAME,
    openapi_url=f"{config.API_PREFIX}/openapi.json",
)

if config.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["OPTIONS", "HEAD", "GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )

app.include_router(professors_router.router, prefix=config.API_PREFIX)
