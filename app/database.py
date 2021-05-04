import motor.motor_asyncio
import os

from bson.objectid import ObjectId

def get_db():
  MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
  MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
  MONGO_DB = os.getenv("MONGO_DB", "database")
  MONGO_NON_ROOT_USERNAME = os.getenv("MONGO_NON_ROOT_USERNAME", "user")
  MONGO_NON_ROOT_PASSWORD_FILE = os.getenv("MONGO_NON_ROOT_PASSWORD_FILE")

  if MONGO_NON_ROOT_PASSWORD_FILE:
    with open(MONGO_NON_ROOT_PASSWORD_FILE, "r") as file:
      MONGO_NON_ROOT_PASSWORD = file.read()
  else:
    MONGO_NON_ROOT_PASSWORD = "Passw0rd"

  uri = f"mongodb://{MONGO_NON_ROOT_USERNAME}:{MONGO_NON_ROOT_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/?authSource={MONGO_DB}"

  print(f"URI={uri}")

  client = motor.motor_asyncio.AsyncIOMotorClient(uri)
  db = client[MONGO_DB]

  return db


db = get_db()
