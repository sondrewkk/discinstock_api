from fastapi import APIRouter, Header, Depends, status
from fastapi.params import Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from bson.objectid import ObjectId

from ..models.disc import DiscModel, CreateDiscModel, UpdateDiscModel
from ..services.disc_service import count_discs, get_discs, get_disc_by_query, create_disc, update_disc
from ..dependencies.query_parameters import CommonQueryParameters, SearchQueryParameters
from ..util.pagination import Pagination
from ..util.link_header import LinkHeader


router = APIRouter(prefix="/discs", tags=["Discs"])


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

    #total: int = await count_discs(commons.in_stock)
    #pagination = Pagination(commons.pagination.skip, commons.pagination.limit, total)
    #link_header = LinkHeader(host, "discs", pagination)

    #headers = {"Link": link_header.get()}
    #response = JSONResponse(content=content, headers=headers)

    response = JSONResponse(content=content)
    return response


@router.get(
    "/search",
    response_description="Search by query",
    response_model=List[DiscModel],
)
async def search_discs(query: SearchQueryParameters = Depends()):
    response = await get_disc_by_query(query)
    return response

@router.post(
    "",
    status_code=201,
    responses={
        201: {"model": DiscModel, "description": "Added new disc"},
        409: {"description": "Disc already exists"},
        401: {"detail": "Not authenticated"},
    },
)
async def add_disc(disc: CreateDiscModel = Body(...)
):
    created_disc = await create_disc(disc)
    content = jsonable_encoder(created_disc, custom_encoder={ObjectId: str})
    response = JSONResponse(status_code=status.HTTP_201_CREATED, content=content)

    return response

@router.patch(
    "/{id}",
    response_model=DiscModel,
)
async def patch_disc(id: str, disc_data: UpdateDiscModel = Body(...)
):
    disc_id: ObjectId = ObjectId(id)
    updated_disc = await update_disc(disc_id ,disc_data)
    content = jsonable_encoder(updated_disc, custom_encoder={ObjectId: str})
    response = JSONResponse(content=content)

    return response
