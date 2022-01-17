import jwt

from fastapi.security.http import HTTPAuthorizationCredentials

from backend.configs import app_config


def verify_token(credentials: HTTPAuthorizationCredentials) -> str:
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

    return str(payload["sub"])
