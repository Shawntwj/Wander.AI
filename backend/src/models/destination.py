from sqlalchemy import Column, String, Float, Text
from .base import BaseModel

class Destination(BaseModel):
    __tablename__ = "destinations"

    name = Column(String, index=True)
    country = Column(String)
    city = Column(String)
    description = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)