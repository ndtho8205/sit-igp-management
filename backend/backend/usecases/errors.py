class AppError(Exception):
    pass


class ConflictError(AppError):
    pass


class NotFoundError(AppError):
    pass


class ForbiddenError(AppError):
    pass


class BadRequestError(AppError):
    pass
