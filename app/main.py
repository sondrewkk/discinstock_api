import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import discs


def get_app():
  app = FastAPI(title="Discinstock_api")

  app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
  )

  # Routes
  app.include_router(discs.router)

  @app.get("/", tags=["Root"])
  async def read_root():
    return {"API to find discgolf discs in stock in diffrent websites where you can buy discs"}

  return app


