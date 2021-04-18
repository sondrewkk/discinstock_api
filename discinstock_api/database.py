import motor.motor_asyncio

from bson.objectid import ObjectId


MONGO_URI = "mongodb://192.168.10.5:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.discgolfspider
