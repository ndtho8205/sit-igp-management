from typing import Iterator

import jwt
from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException

from backend.configs import app_config
from backend.usecases import verify_professor_email
from backend.adapters.pg import professor_repository
from backend.drivers.pg.session import DbSession
from backend.entities.professor import Professor


def get_db() -> Iterator[Session]:
    db_session = DbSession()
    try:
        yield db_session
    finally:
        db_session.close()
        print("DbSession was closed!")


auth_scheme = HTTPBearer()


def verify_token(credentials: HTTPAuthorizationCredentials) -> str:
    return "nb20501@shibaura-it.ac.jp"
    jwks_url = f"https://{app_config.AUTH_DOMAIN}/.well-known/jwks.json"
    jwks_client = jwt.PyJWKClient(jwks_url)

    signing_key = jwks_client.get_signing_key_from_jwt(credentials.credentials).key

    payload = jwt.decode(
        credentials.credentials,
        signing_key,
        algorithms=[app_config.AUTH_ALGORITHMS],
        audience=app_config.AUTH_API_AUDIENCE,
        issuer=app_config.AUTH_ISSUER,
    )
    print(payload)

    return str(payload["sub"])


def authenticate_user(
    db_session: Session = Depends(get_db),
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
) -> Professor:
    try:
        user_email = verify_token(token)
    except Exception as ex:
        raise HTTPException(
            status_code=401,
            detail="Incorrect login information",
        ) from ex

    professor_repository.set_session(db_session)
    user = verify_professor_email(professor_repository, user_email)
    print(user)

    if not user or user.is_deleted:
        raise HTTPException(
            status_code=401,
            detail="Incorrect login information",
        )

    return user
