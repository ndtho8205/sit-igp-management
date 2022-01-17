from typing import List, Tuple

from pydantic.error_wrappers import ErrorWrapper

from fastapi import status
from fastapi.exceptions import HTTPException, RequestValidationError


class AppException(HTTPException):
    pass


class ValidationError(RequestValidationError):
    def __init__(self, error_list: List[Tuple[str, str]]) -> None:
        errors = [
            ErrorWrapper(ValueError(error[1]), loc=("body", error[0]))
            for error in error_list
        ]
        super().__init__(errors)


class NotFoundError(AppException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The requested resource was not found",
        )


class ConflictError(AppException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)


class ForbiddenError(AppException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access rights to the requested resource",
        )


class UnauthorizedError(AppException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication is required for the requested resource",
        )
