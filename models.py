from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    title: str
    link: str
    image: str
    current_price: float
    target_price: Optional[float] = None

class PriceHistory(BaseModel):
    product_id: str
    price: float
    date: datetime