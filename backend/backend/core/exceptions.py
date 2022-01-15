from fastapi.exceptions import HTTPException


class AppException(HTTPException):
    pass


class ResourceNotFoundError(AppException):
    def __init__(self, resource_name: str) -> None:
        super().__init__(status_code=404, detail=f"The {resource_name} was not found")


class AuthError(AppException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=403, detail=detail)
