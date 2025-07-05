from typing import Optional, List
from pydantic import BaseModel, computed_field
from datetime import datetime


class OrderItem(BaseModel):
    product_id: int
    name: str
    price: int
    quantity: int = 1


class Order(BaseModel):
    created_at: datetime = datetime.now()
    order_items: Optional[List[OrderItem]]

    @computed_field
    def total_cost(self) -> int:
        total_cost = 0
        for order_item in self.order_items:
            total_cost += order_item.price * order_item.quantity
        return total_cost
