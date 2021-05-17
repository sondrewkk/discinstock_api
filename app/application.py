from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routes
from .routers import root
from .routers import discs

class Application():
    
    def __init__(self, title="Application"):
        self._app = FastAPI(title=title)
        
        # Middleware
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )

        # Routes
        self._app.include_router(root.router)
        self._app.include_router(discs.router)

    def get_app(self):
        return self._app 