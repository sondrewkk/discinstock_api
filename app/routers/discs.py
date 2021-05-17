from fastapi import APIRouter
from typing import List, Optional

from fastapi.params import Query

#from ..database import db
from ..models.disc import DiscModel
from ..services.disc_service import get_discs, get_disc_by_name


router = APIRouter(prefix="/discs")

@router.get(
  "", 
  response_description="List all discs", 
  response_model=List[DiscModel])
async def list_discs(in_stock: Optional[bool] = True, skip: int = 0, limit: int = 50):
  response = await get_discs(in_stock, skip, limit)
  return response

@router.get(
  "/search", 
  response_description="Search after disc by name", 
  response_model=List[DiscModel])
async def get_disc(name: str = Query(None, min_length=3)):
  response = await get_disc_by_name(name)
  return response