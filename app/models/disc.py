from typing import Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from datetime import datetime

from .pyobjectid import PyObjectId


class DiscModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    image: str
    spider_name: str
    in_stock: bool
    url: str
    retailer: str
    retailer_id: str
    brand: str
    price: int
    speed: Optional[float]
    glide: Optional[float]
    turn: Optional[float]
    fade: Optional[float]
    created: datetime
    last_updated: datetime


    class Config:
        allow_population_by_field_name = (True,)
        arbitrary_types_allowed = (True,)
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": "607a1d5406f9d87ebea936d5",
                "name": "K3 Reko",
                "image": "https://www.dgshop.no/pub/media/catalog/product/cache/873ab35ce770a8e6abb698435365a0d0/r/e/reko_k3_b.png",
                "url": "https://www.dgshop.no/k3-reko",
                "spider_name": "dgshop",
                "in_stock": "true",
                "retailer": "dgshop.no",
                "retailer_id": "aHR0cHM6Ly93d3cudGJrc3BvcnQubm8va2FzdGFwbGFzdC1qYXJuLTQv",
                "brand": "Kastaplast",
                "price": "145",
                "speed": "3",
                "glide": "3",
                "turn": "0",
                "fade": "1",
                "created": "2021-08-11T23:14:48.920Z",
                "last_update": "2021-08-11T23:14:48.920Z",
            }
        }

class CreateDiscModel(BaseModel):
    name: str
    image: str
    spider_name: str
    in_stock: bool
    url: str
    retailer: str
    retailer_id: str
    brand: str
    price: int
    speed: Optional[float]
    glide: Optional[float]
    turn: Optional[float]
    fade: Optional[float]

class UpdateDiscModel(BaseModel):
    name: Optional[str]
    image: Optional[str]
    spider_name: Optional[str]
    in_stock: Optional[bool]
    url: Optional[str]
    retailer: Optional[str]
    retailer_id: Optional[str]
    brand: Optional[str]
    price: Optional[int]
    speed: Optional[float]
    glide: Optional[float]
    turn: Optional[float]
    fade: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "in_stock": "true"
            }
        }
