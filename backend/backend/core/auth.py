import jwt
from sqlalchemy.orm.session import Session

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException

from backend.configs import app_config
from backend.dependencies import get_db
from backend.api.professors import service as professors_service
from backend.core.exceptions import AuthError
from backend.api.professors.professors_entities import Professor


auth_scheme = HTTPBearer()


def authenticate_professor(
    db_session: Session = Depends(get_db),
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
) -> Professor:
    user_email = _verify_token(token)
    user = professors_service.find_one_by_email(db_session, user_email)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect login information")
    return Professor.from_orm(user)


def _verify_token(credentials: HTTPAuthorizationCredentials) -> str:
    jwks_url = f"https://{app_config.AUTH_DOMAIN}/.well-known/jwks.json"
    jwks_client = jwt.PyJWKClient(jwks_url)

    try:
        signing_key = jwks_client.get_signing_key_from_jwt(credentials.credentials).key
    except jwt.exceptions.PyJWKClientError as error:
        raise AuthError("Invalid token or expired token") from error
    except jwt.exceptions.DecodeError as error:
        raise AuthError(str(error)) from error

    try:
        payload = jwt.decode(
            credentials.credentials,
            signing_key,
            algorithms=[app_config.AUTH_ALGORITHMS],
            audience=app_config.AUTH_API_AUDIENCE,
            issuer=app_config.AUTH_ISSUER,
        )
    except Exception as error:
        raise AuthError(str(error)) from error

    return str(payload["sub"])
