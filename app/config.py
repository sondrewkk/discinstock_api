from os import getenv
from .util.docker_secret import get_secret
from dotenv import load_dotenv


class Settings:
    load_dotenv()

    app_title: str = "Discinstock API"
    mongo_host = getenv("MONGO_HOST")
    mongo_port = int(getenv("MONGO_PORT", 27017))
    mongo_db = getenv("MONGO_DB")
    mongo_non_root_username = getenv("MONGO_NON_ROOT_USERNAME")
    mongo_non_root_password = get_secret("MONGO_NON_ROOT_PASSWORD_FILE")
