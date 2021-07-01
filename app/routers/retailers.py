from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.params import Body

from ..services.retailer_service import get_retailers, create_retailer
from ..models.retailer import AddRetailerModel, RetailerModel


router = APIRouter(prefix="/retailers", tags=["Retailers"])

@router.get(
    "", 
    response_description="List all retailers",
    response_model=List[RetailerModel],
)
async def list_retailers(
):
    response = await get_retailers() 
    
    return response
    
@router.post(
    "",
    status_code=201,
    responses={ 
        201: { "model": RetailerModel, "description": "Added new retailer" }, 
        409: { "description": "Retailer already exists" }
    },
    response_model_exclude={"_id"},
)
async def add_retailer(retailer: AddRetailerModel = Body(...)
):
    retailer = jsonable_encoder(retailer)
    created_retailer = await create_retailer(retailer)
    
    return created_retailer
