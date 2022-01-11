from fastapi.exceptions import HTTPException


class AppException(HTTPException):
    pass


class ResourceNotFoundError(AppException):
    def __init__(self, resource_name: str) -> None:
        super().__init__(status_code=404, detail=f"{resource_name} not found")
