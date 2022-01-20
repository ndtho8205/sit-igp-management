from typing import Iterator

import jwt
from sqlalchemy.orm import Session

from fastapi import Depends, status
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


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> str:
    jwks_url = f"https://{app_config.AUTH_DOMAIN}/.well-known/jwks.json"
    jwks_client = jwt.PyJWKClient(jwks_url)

    try:
        signing_key = jwks_client.get_signing_key_from_jwt(credentials.credentials).key
    except Exception as ex:
        print(str(ex))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials"
        ) from ex

    try:
        payload = jwt.decode(
            credentials.credentials,
            signing_key,
            algorithms=[app_config.AUTH_ALGORITHMS],
            audience=app_config.AUTH_API_AUDIENCE,
            issuer=app_config.AUTH_ISSUER,
        )
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials"
        ) from ex

    return str(payload[app_config.AUTH_EMAIL_NAMESPACE])


def authenticate_user(
    db_session: Session = Depends(get_db),
    user_email: str = Depends(verify_token),
) -> Professor:
    professor_repository.set_session(db_session)
    user = verify_professor_email(professor_repository, user_email)

    if not user or user.is_deleted:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please login using your university email account.",
        )

    return user
