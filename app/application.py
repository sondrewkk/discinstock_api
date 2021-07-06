from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routes
from .routers import root
from .routers import discs
from .routers import brands
from .routers import retailers
from .routers import authorization


class Application:
    def __init__(self, title="Application"):
        self._app = FastAPI(title=title)

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
        self._app.include_router(authorization.router)
        self._app.include_router(discs.router)
        self._app.include_router(brands.router)
        self._app.include_router(retailers.router)

    def get_app(self):
        return self._app
