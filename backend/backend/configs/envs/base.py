from typing import Any, Dict, List, Optional

from enum import Enum

from pydantic import AnyHttpUrl, BaseSettings, validator
from pydantic.networks import HttpUrl, PostgresDsn

from backend.entities.types import FullName, UniversityEmailStr


class AppEnvTypes(Enum):
    PROD = "prod"
    DEV = "dev"
    TEST = "test"


class BaseConfig(BaseSettings):
    # pylint: disable=invalid-name

    APP_ENV: AppEnvTypes

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        allow_mutation = False


class BaseAppConfig(BaseConfig):
    # pylint: disable=invalid-name

    AUTH_DOMAIN: str
    AUTH_API_AUDIENCE: str
    AUTH_ALGORITHMS: str
    AUTH_ISSUER: HttpUrl
    AUTH_EMAIL_NAMESPACE: str

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    DATABASE_URL: Optional[PostgresDsn] = None

    @validator("DATABASE_URL", pre=True, always=True)
    def assemble_database_url(  # pylint: disable=no-self-argument, no-self-use
        cls,  # noqa: B902, N805
        v: Optional[str],
        values: Dict[str, Any],
    ) -> str:
        """Build SQLAlchemy URI."""
        if isinstance(v, str):
            if v.startswith("postgres://"):
                v = v.replace("postgres://", "postgresql://", 1)
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

    APP_NAME: str = "SIT IGP Management"
    API_PREFIX: str = "/api"

    CORS_ALLOW_ORIGINS: List[AnyHttpUrl] = []

    SENTRY_DSN: Optional[HttpUrl] = None

    SUPERUSER_FULLNAME: FullName
    SUPERUSER_EMAIL: UniversityEmailStr
