from fastapi import APIRouter
from ..services.brand_service import get_brands


router = APIRouter(prefix="/brands")

@router.get(
    "", 
    response_description="List all brands",
)
async def list_brands():
    response = await get_brands()
    
    return response