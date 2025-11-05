from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class PriceHistorySchema(BaseModel):
    price: float
    date: datetime

    class Config:
        orm_mode = True

class ProductCreateSchema(BaseModel):
    title: str
    link: str
    image: str
    current_price: float
    target_price: Optional[float] = None

class ProductSchema(BaseModel):
    id: int
    title: str
    link: str
    image: str
    current_price: float
    target_price: Optional[float] = None
    price_history: List[PriceHistorySchema] = []

    class Config:
        orm_mode = True
