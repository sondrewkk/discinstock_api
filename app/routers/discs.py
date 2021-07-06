from fastapi import APIRouter, Header, Depends
from fastapi.params import Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from bson.objectid import ObjectId

from ..models.disc import DiscModel
from ..services.disc_service import count_discs, get_discs, get_disc_by_name
from ..dependencies.query_parameters import CommonQueryParameters
from ..util.pagination import Pagination
from ..util.link_header import LinkHeader


router = APIRouter(prefix="/discs")


@router.get(
    "", response_description="List all discs", response_model=List[DiscModel],
)
async def list_discs(
    host: str = Header(None), commons: CommonQueryParameters = Depends(),
):
    data = await get_discs(
        commons.in_stock, commons.pagination.skip, commons.pagination.limit
    )
    content = jsonable_encoder(data, custom_encoder={ObjectId: str})

    total: int = await count_discs(commons.in_stock)
    pagination = Pagination(commons.pagination.skip, commons.pagination.limit, total)
    link_header = LinkHeader(host, "discs", pagination)

    headers = {"Link": link_header.get()}
    response = JSONResponse(content=content, headers=headers)

    return response


@router.get(
    "/search",
    response_description="Search after disc by name",
    response_model=List[DiscModel],
)
async def get_disc(name: str = Query(None, min_length=2)):
    response = await get_disc_by_name(name)
    return response
