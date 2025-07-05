from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: int
    description: Optional[str]


class ResponseProduct(Product):
    id: int
