from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import api
from backend.configs.envs.base import BaseAppConfig


def init_app(config: BaseAppConfig) -> FastAPI:
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
