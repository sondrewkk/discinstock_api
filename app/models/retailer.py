from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from .pyobjectid import PyObjectId


class RetailerModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    link: str = Field(...)
    logo: str = Field(...)
    country: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": "60ddae8f79f7195fde93a4f7",
                "name": "dgshop.no",
                "link": "https://www.dgshop.no/",
                "logo": "https://www.dgshop.no/pub/media/logo/websites/1/dgshop_hovedbanner.png",
                "country": "no",
            }
        }


class AddRetailerModel(BaseModel):
    name: str = Field(...)
    link: str = Field(...)
    logo: str = Field(...,)
    country: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "dgshop.no",
                "link": "https://www.dgshop.no/",
                "logo": "https://www.dgshop.no/pub/media/logo/websites/1/dgshop_hovedbanner.png",
                "country": "no",
            }
        }
