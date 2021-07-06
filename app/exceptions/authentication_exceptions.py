from fastapi.exceptions import HTTPException
from fastapi import status


class CredentialsException(HTTPException):
    def __init__(self) -> None:
        detail = "Could not validate credentials"
        headers = {"WWW-Authenticate": "Bearer"}
        status_code = status.HTTP_401_UNAUTHORIZED

        super().__init__(status_code=status_code, detail=detail, headers=headers)


class IncorrectUsernameOrPasswordException(HTTPException):
    def __init__(self) -> None:
        detail = "Incorrect username or password"
        headers = {"WWW-Authenticate": "Bearer"}
        status_code = status.HTTP_401_UNAUTHORIZED

        super().__init__(status_code=status_code, detail=detail, headers=headers)
