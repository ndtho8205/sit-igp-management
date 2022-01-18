from starlette import status
from sqlalchemy.orm.session import Session

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException

from backend.core.auth import verify_token
from backend.dependencies import get_db
from backend.api.professors.professors_dto import ProfessorUpdateDto
from backend.api.professors.professors_service import service as professors_service
from backend.api.professors.professors_entities import Professor


auth_scheme = HTTPBearer()


def authenticate_user(
    db_session: Session = Depends(get_db),
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
) -> Professor:
    # try:
    #     user_email = verify_token(token)
    # except Exception as ex:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Incorrect login information",
    #     ) from ex

    user = professors_service.find_one_by_email(db_session, "tanpx@shibaura-it.ac.jp")

    if not user or user.is_deleted:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have enough privileges",
        )
    if not user.is_verified:
        user.is_verified = True
        professors_service.update_by_id(
            db_session,
            user.id_,
            ProfessorUpdateDto(is_verified=True),
        )
    return Professor.from_orm(user)


def get_normal_user(user: Professor = Depends(authenticate_user)) -> Professor:
    return user


def get_superuser(user: Professor = Depends(authenticate_user)) -> Professor:
    if not user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have enough privileges",
        )
    return user
