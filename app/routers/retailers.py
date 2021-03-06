from typing import List
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends
from fastapi.params import Body
from fastapi.responses import JSONResponse
from bson.objectid import ObjectId

from ..services.retailer_service import get_retailers, create_retailer
from ..models.retailer import AddRetailerModel, RetailerModel
from ..services.auth_service import validate_token


router = APIRouter(prefix="/retailers", tags=["Retailers"])


@router.get(
    "", response_description="List all retailers", response_model=List[RetailerModel],
)
async def list_retailers():
    response = await get_retailers()

    return response


@router.post(
    "",
    status_code=201,
    responses={
        201: {"model": RetailerModel, "description": "Added new retailer"},
        409: {"description": "Retailer already exists"},
        401: {"detail": "Not authenticated"},
    },
)
async def add_retailer(
    retailer: AddRetailerModel = Body(...), valid: bool = Depends(validate_token)
):
    retailer = jsonable_encoder(retailer)
    created_retailer = await create_retailer(retailer)

    content = jsonable_encoder(created_retailer, custom_encoder={ObjectId: str})
    response = JSONResponse(status_code=status.HTTP_201_CREATED, content=content)

    return response
