from fastapi.exceptions import HTTPException
from ..database import Database
from ..config import Settings

config = Settings()
client = Database(config).get_client()

db_name = config.mongo_db
db = client[db_name]


async def get_retailers():
    retailers = await db["retailers"].find({}).to_list(100)

    return retailers


async def create_retailer(retailer):
    exists = await db["retailers"].find_one({"name": retailer["name"]})

    if exists:
        raise HTTPException(status_code=409, detail="Retailer already exists.")

    result = await db["retailers"].insert_one(retailer)
    created_retailer = await db["retailers"].find_one({"_id": result.inserted_id})

    return created_retailer
