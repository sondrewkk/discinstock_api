from pydantic import BaseModel, Field
from bson.objectid import ObjectId

from .pyobjectid import PyObjectId


class DiscModel(BaseModel):
  id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
  name: str = Field(...)
  image: str = Field(...)
  spider_name: str = Field(...)
  in_stock: bool = Field(...)
  url: str = Field(...)
  retailer: str = Field(...)

  class Config:
    allow_population_by_field_name = True,
    arbitrary_types_allowed = True,
    json_encoders = {ObjectId: str}
    schema_extra = {
      "example": {
        "_id": "607a1d5406f9d87ebea936d5",
        "name": "K3 Berg",
        "image": "https://www.dgshop.no/pub/media/catalog/product/cache/873ab35ce770a8e6abb698435365a0d0/b/e/berg_k3_b.jpg",
        "spider_name": "dgshop",
        "in_stock": True,
        "url": "https://www.dgshop.no/k3-berg",
        "retailer": "dgshop.no"
      }
    }
  