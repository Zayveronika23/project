from sqlalchemy import Column, Integer, String, Date, Boolean, Text
from .db import Base


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)