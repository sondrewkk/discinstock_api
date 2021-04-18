import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import discs

app = FastAPI()


# CORS
origins = {
  "http://localhost:8081"
}

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)


# Routes
app.include_router(discs.router)

@app.get("/", tags=["Root"])
async def read_root():
  return {"API to find discgolf discs in stock in diffrent websites where you can buy discs"}

def start():
  """Launched with `poetry run start` at root level"""
  uvicorn.run("discinstock_api.main:app", host="0.0.0.0", port=8000, reload=True)