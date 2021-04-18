from fastapi import APIRouter, Query
from typing import List, Optional

from ..database import db
from ..models.disc import DiscModel

router = APIRouter()


@router.get("/discs", response_description="List all discs", response_model=List[DiscModel])
async def list_discs(in_stock: Optional[bool] = True, skip: int = 0, limit: int = 50):
  query = {}
  
  if in_stock is not None:
    query["in_stock"] = in_stock

  discs = await db["discs"].find(query).limit(limit).skip(skip).to_list(limit)
  return discs

@router.get(
  "/discs/search/", 
  response_description="Search after disc by name", 
  response_model=List[DiscModel])
async def get_disc(name: str, exact: Optional[bool] = False, in_stock: Optional[bool] = True):
  query = {
    "name": {"$regex": name, "$options": "i"},
    "in_stock": in_stock
  }
  
  discs = await db["discs"].find(query).to_list(50)
  return discs