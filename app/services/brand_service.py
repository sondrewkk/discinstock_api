import motor
from pymongo.collation import Collation 
from ..database import Database
from ..config import Settings


config = Settings()
client = Database(config).get_client()

db_name = config.mongo_db
db = client[db_name]


async def get_brands(
):
    # Get a list of brands, where disc is in stock, sorted alphabetically.
    distinct_brands_pipeline = [
    {
        '$group': {
            '_id': None, 
            'name': {
                '$addToSet': {
                    '$cond': {
                        'if': '$in_stock', 
                        'then': '$brand', 
                        'else': '$$REMOVE'
                    }
                }
            }
        }
        }, {
            '$unwind': {
                'path': '$name'
            }
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

    collation = Collation("en", strength=2)

    brands = await db["discs"].aggregate(distinct_brands_pipeline, collation=collation).to_list(100)

    return brands
