from pydantic import BaseModel, Field
from bson.objectid import ObjectId

from .pyobjectid import PyObjectId


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    hashed_password: str

    class Config:
        allow_population_by_field_name = (True,)
        arbitrary_types_allowed = (True,)
        json_encoders = {ObjectId: str}
