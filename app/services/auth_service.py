from typing import Optional
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime

from ..models.user import User
from ..models.token import TokenData
from ..config import Settings
from ..database import Database
from ..exceptions.authentication_exceptions import (
    CredentialsException,
    IncorrectUsernameOrPasswordException,
)


config = Settings()

client = Database(config).get_client()
db_name = config.mongo_db
db = client[db_name]

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_access_token_expire_minutes() -> int:
    return config.access_token_expire_minutes


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def get_user(username: str) -> User:
    user: User = await db["users"].find_one({"username": username})
    return user


async def authenticate_user(username: str, password: str) -> User:
    user = await get_user(username)

    if not user:
        raise IncorrectUsernameOrPasswordException()

    verified_password = verify_password(password, user["hashed_password"])

    if not verified_password:
        raise IncorrectUsernameOrPasswordException()

    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, config.jwt_secret_key, algorithm=config.algorithm
    )
    return encoded_jwt


async def validate_token(token: str = Depends(oauth2_schema)) -> bool:
    try:
        payload = jwt.decode(
            token, config.jwt_secret_key, algorithms=[config.algorithm]
        )
        username: str = payload.get("sub")

        if username is None:
            raise CredentialsException()

        token_data = TokenData(username=username)
    except JWTError:
        raise CredentialsException()

    user = await get_user(username=token_data.username)

    if user is None:
        raise CredentialsException()

    return True
