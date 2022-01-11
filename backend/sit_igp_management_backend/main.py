from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sit_igp_management_backend.api import api
from sit_igp_management_backend.db.init_db import init_db
from sit_igp_management_backend.core.config import config


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

app.include_router(api.router, prefix=config.API_PREFIX)
