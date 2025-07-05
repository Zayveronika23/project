from sqlalchemy import Column, Integer, String, Date, Boolean, Text, ForeignKey
from .db import Base
from sqlalchemy.orm import relationship


class OrderItemModel(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer)
    name = Column(String)
    price = Column(Integer)
    order = relationship("OrderModel", back_populates="order_items")


class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_items = relationship("OrderItemModel", back_populates="order",
                               cascade="all, delete-orphan")
    total_cost = Column(Integer)
    created_at = Column(Date)