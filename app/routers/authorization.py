from datetime import timedelta
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..models.token import Token
from ..models.user import User
from ..services.auth_service import (
    authenticate_user,
    get_access_token_expire_minutes,
    create_access_token,
)


router = APIRouter(tags=["Authorization"])


@router.post("/token", response_model=Token)
async def authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    user: User = await authenticate_user(form_data.username, form_data.password)
    access_token_expires = timedelta(minutes=get_access_token_expire_minutes())

    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )

    token = Token(access_token=access_token, token_type="bearer")

    return token
