from ..database import Database
from ..config import Settings

config = Settings()
client = Database(config).get_client()

db_name = config.mongo_db
db = client[db_name]

async def get_retailers():
    distinct_retailer_pipeline = [
        {
            '$group': {
                '_id': None, 
                'name': {
                    '$addToSet': '$retailer'
                }
            }
        }, {
            '$project': {
                '_id': False
            }
        }, {
            '$unwind': {
                'path': '$name'
            }
        }
    ]

    retailers = await db["discs"].aggregate(distinct_retailer_pipeline).to_list(100)

    return retailers
