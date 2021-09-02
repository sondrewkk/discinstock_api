from datetime import datetime
from bson.objectid import ObjectId
from fastapi.exceptions import HTTPException
from typing import List
from pymongo.results import UpdateResult, InsertOneResult

from ..database import Database
from ..config import Settings
from ..models.disc import CreateDiscModel, DiscModel, UpdateDiscModel
from ..exceptions.disc_exceptions import DiscNotCreatedException, DiscNotFoundException, DiscNotUpdatedException
from ..dependencies.query_parameters import SearchQueryParameters


config = Settings()
client = Database(config).get_client()

db_name = config.mongo_db
db = client[db_name]


async def get_discs(in_stock: bool, skip: int, limit: int
) -> List[DiscModel]:
    query = {"in_stock": in_stock}

    discs: List[DiscModel] = await db["discs"].find(query).limit(limit).skip(
        skip
    ).to_list(limit)
    return discs


async def get_disc_by_query(query: SearchQueryParameters
) -> List[DiscModel]:
    query = query.dict()
    discs: List[DiscModel] = await db["discs"].find(query).to_list(5000)
    return discs


async def get_disc_by_id(id: ObjectId
) -> DiscModel:
    disc: DiscModel = await db["discs"].find_one({"_id": id})
    return disc


async def count_discs(in_stock: bool = True
) -> int:
    count = await db["discs"].count_documents({"in_stock": in_stock})
    return count


async def create_disc(disc: CreateDiscModel
) -> DiscModel:
    # Check if the disc is already stored in the database
    exists = await db["discs"].find_one({
        "name": disc.name, 
        "spider_name": disc.spider_name,
    })

    # Return an error if it it
    if exists:
        raise HTTPException(status_code=409, detail="Disc already exists.")

    # Convert to dict and add timestamps for created and last_updated
    disc = disc.dict()
    disc["created"] = datetime.now()
    disc["last_updated"] = datetime.now()

    # Insert in database, and check if write operation is okey
    result: InsertOneResult = await db["discs"].insert_one(disc)

    # Return an error if it fails
    if not result.acknowledged:
        raise DiscNotCreatedException(disc.name)

    # Return the created disc if it is added to database
    created_disc = await db["discs"].find_one({ "_id": result.inserted_id })
    return created_disc


async def update_disc(id: ObjectId, disc: UpdateDiscModel
) -> DiscModel: 
    # Check if the disc is already stored in database
    stored_disc: DiscModel = await db["discs"].find_one({"_id": id})
    if not stored_disc:
        raise DiscNotFoundException(id)

    # Create an dict only with the keys to update
    update_data = disc.dict(exclude_unset=True)

    # In stock is the only key that triggers a last_update update
    if "in_stock" in update_data.keys() and stored_disc['in_stock'] != update_data['in_stock']:
        update_data["last_updated"] = datetime.now()

    # Write over selected key and 
    result: UpdateResult = await db["discs"].update_one({"_id": id}, {"$set": update_data})

    if result.modified_count == 0:
        return DiscNotUpdatedException(id)

    # Return if update is confirmed
    updated_disc: DiscModel = await db["discs"].find_one({"_id": id})
    return updated_disc
    