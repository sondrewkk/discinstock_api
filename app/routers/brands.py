from fastapi import APIRouter
from typing import List

from ..services.brand_service import get_brands
from ..models.brand import BrandModel


router = APIRouter(prefix="/brands")


@router.get(
    "",
    response_description="List all brands. Response is sorted by name.",
    response_model=List[BrandModel],
)
async def list_brands():
    response = await get_brands()

    return response
