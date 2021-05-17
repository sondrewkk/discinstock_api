#from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware

#from .routers import discs

from .database import Database
from .config import Settings
from .application import Application


# Load configuration
config = Settings()

# Crate an application instance
fastapi_application = Application(config.app_title)

# Expose app server
app= fastapi_application.get_app()
