from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Root"])
async def read_root():
    return {"See /docs for more information about this API"}
