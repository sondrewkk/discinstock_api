from ..database import Database
from ..config import Settings
from ..models.disc import DiscModel
from typing import List

config = Settings()
client = Database(config).get_client()

db_name = config.mongo_db
db = client[db_name]

async def get_discs(in_stock: bool, skip: int, limit: int):   
    query = {
        "in_stock": in_stock
    }

    discs: List[DiscModel] = await db["discs"].find(query).limit(limit).skip(skip).to_list(limit)
    return discs

async def get_disc_by_name(name: str):
    query = {
        "name": {"$regex": name, "$options": "i"},
        "in_stock": True
    }

    discs: List[DiscModel] = await db["discs"].find(query).to_list(50)
    return discs
