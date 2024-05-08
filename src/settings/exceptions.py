from fastapi import HTTPException, status


class DetailedHTTPException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Server error"

    def __init__(self, **kwargs) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail, **kwargs)


class DatabaseExceptions(DetailedHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Database exceptions, contact with api support."


class BadToken(DetailedHTTPException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Bad Token."
