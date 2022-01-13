from typing import Any, Dict, List, Optional

import secrets

from pydantic import AnyHttpUrl, BaseSettings, validator
from pydantic.networks import HttpUrl, PostgresDsn


class Config(BaseSettings):
    # pylint: disable=invalid-name

    AUTH_DOMAIN: str
    AUTH_API_AUDIENCE: str
    AUTH_ALGORITHMS: str
    AUTH_ISSUER: HttpUrl

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True, always=True)
    def assemble_uri(  # pylint: disable=no-self-argument, no-self-use
        cls,  # noqa: B902, N805
        v: Optional[str],
        values: Dict[str, Any],
    ) -> str:
        """Build SQLAlchemy URI."""
        if isinstance(v, str):
            return v
        return str(
            PostgresDsn.build(
                scheme="postgresql",
                user=values.get("POSTGRES_USER"),
                password=values.get("POSTGRES_PASSWORD"),
                host=values.get("POSTGRES_SERVER"),
                path=f"/{values.get('POSTGRES_DB')}",
            )
        )

    SMTP_TLS: bool = True
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None

    APP_NAME: str = "SIT IGP Management"
    API_PREFIX: str = "/api"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 8 * 24 * 60
    SECRET_KEY: str = secrets.token_urlsafe(32)
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    SENTRY_DSN: Optional[HttpUrl] = None

    class Config:
        case_sensitive = True


config = Config()
