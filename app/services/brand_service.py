from ..database import Database
from ..config import Settings

config = Settings()
client = Database(config).get_client()

db_name = config.mongo_db
db = client[db_name]

async def get_brands():
    distinct_brands_pipeline = [
        {
            '$group': {
                '_id': None, 
                'brand': {
                    '$addToSet': '$brand'
                }
            }
        }, {
            '$unwind': '$brand'
        }, {
            '$sort': {
                'brand': 1
            }
        }, {
            '$group': {
                '_id': None, 
                'brands': {
                    '$push': '$brand'
                }
            }
        }, {
            '$project': {
                '_id': False
            }
        }
    ]  

    brands = await db["discs"].aggregate(distinct_brands_pipeline).next()

    return brands