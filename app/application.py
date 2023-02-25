from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.util.validate_token import validate_token

# Import routes
from .routers import root
from .routers import discs
from .routers import brands
from .routers import retailers


class Application:
    def __init__(self, title="Application"):
        self._app = FastAPI(title=title, dependencies=[Depends(validate_token)])

        # Middleware
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["link"],
        )

        # Routes
        self._app.include_router(root.router)
        self._app.include_router(discs.router)
        self._app.include_router(brands.router)
        self._app.include_router(retailers.router)

    def get_app(self):
        return self._app
