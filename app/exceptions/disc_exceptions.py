from bson.objectid import ObjectId
from fastapi.exceptions import HTTPException
from fastapi import status


class DiscNotFoundException(HTTPException):
    def __init__(self, id: ObjectId) -> None:
        detail = f"Disc {id} not found."
        headers = {"WWW-Authenticate": "Bearer"}
        status_code = status.HTTP_404_NOT_FOUND

        super().__init__(status_code=status_code, detail=detail, headers=headers)

class DiscNotCreatedException(HTTPException):
    def __init__(self, name: str) -> None:
        detail = f"{name.capitalize} is not created."
        headers = {"WWW-Authenticate": "Bearer"}
        status_code = status.HTTP_400_BAD_REQUEST

        super().__init__(status_code=status_code, detail=detail, headers=headers)

class DiscNotUpdatedException(HTTPException):
    def __init__(self, id: ObjectId) -> None:
        detail = f"Disc {id} not updated."
        headers = {"WWW-Authenticate": "Bearer"}
        status_code = status.HTTP_400_BAD_REQUEST

        super().__init__(status_code=status_code, detail=detail, headers=headers)