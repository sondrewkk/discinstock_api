import motor.motor_asyncio
from bson.objectid import ObjectId


class Database:
    client = None

    def __init__(self, config):
        self.config = config

        if not self.client:
            self.client = self.__create_db_client()

    def __create_db_client(self):
        uri = f"mongodb://{self.config.mongo_host}:{self.config.mongo_port}"

        if self.config.mongo_non_root_username:
            uri = f"mongodb://{self.config.mongo_non_root_username}:{self.config.mongo_non_root_password}@{self.config.mongo_host}:{self.config.mongo_port}/?authSource={self.config.mongo_db}"

        client = motor.motor_asyncio.AsyncIOMotorClient(uri)

        if not client:
            print("Could'ent create database client")
            return None

        return client

    def get_client(self):
        return self.client
