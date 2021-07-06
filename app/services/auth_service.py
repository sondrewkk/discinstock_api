from typing import Optional
from fastapi import status, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime

from ..models.user import UserInDB, User
from ..models.token import TokenData


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


oauth2_schema = OAuth2PasswordBearer(tokenUrl="/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
db = {
    "discinstock": {
        "username": "discinstock",
        "hashed_password": "$2b$12$krJKHaC.bjy86laqZlxqYORBhd2SROsrZ7CaJ4RgAHrlovxXQkj/C",
    }
}

secret_key = "9e077309686c8657e9e6f91108f492d7091cade20ba29b40e19ed6ea6a8e8e34"
algorithm = "HS256"
access_token_expire_minutes = 30


def get_access_token_expire_minutes() -> int:
    return access_token_expire_minutes


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def get_user(username: str) -> UserInDB:
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(username: str, password: str) -> User:
    user = get_user(username)

    if not user:
        raise IncorrectUsernameOrPasswordException()

    verified_password = verify_password(password, user.hashed_password)

    if not verified_password:
        raise IncorrectUsernameOrPasswordException()

    return User(username=user.username)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


async def validate_token(token: str = Depends(oauth2_schema)) -> bool:
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")

        if username is None:
            raise CredentialsException()

        token_data = TokenData(username=username)
    except JWTError:
        raise CredentialsException()

    user = get_user(username=token_data.username)
    if user is None:
        raise CredentialsException()

    return True
