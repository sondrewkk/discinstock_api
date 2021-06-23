from typing import List
from fastapi import APIRouter

from ..services.retailer_service import get_retailers
from ..models.retailer import RetailerModel


router = APIRouter(prefix="/retailers")

@router.get(
    "", 
    response_description="List all retailers",
    response_model=List[RetailerModel]
)
async def list_retailers():
    response = await get_retailers()
    
    return response
    