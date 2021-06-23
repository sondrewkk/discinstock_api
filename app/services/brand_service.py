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
                'name': {
                    '$addToSet': '$brand'
                }
            }
        }, {
            '$unwind': '$name'
        }, {
            '$sort': {
                'name': 1
            }
        }, {
            '$project': {
                '_id': False
            }
        }
    ]

    brands = await db["discs"].aggregate(distinct_brands_pipeline).to_list(100)

    return brands