from fastapi import FastAPI
from ..db.db import Base, engine
from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker
from ..db.models import ProductModel
from ..schemas.schemas import Product, ResponseProduct

Base.metadata.create_all(bind=engine)

app = FastAPI()


SessionLocal = sessionmaker(autoflush=False, bind=engine)

router = APIRouter()


@router.get("/{product_id}")
def get_product(product_id) -> ResponseProduct:
    db = SessionLocal()
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        return 'Товар не найден'
    return product


@router.get("/")
def get_catalog() -> list[ResponseProduct]:
    db = SessionLocal()
    return db.query(ProductModel).all()


@router.post("/")
def create_product(product: Product) -> ResponseProduct:
    db = SessionLocal()
    new_product = ProductModel(
        name=product.name,
        price=product.price,
        description=product.description)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.delete("/{product_id}")
def delete_product(product_id):
    db = SessionLocal()
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        return 'Продукт не найден'
    db.delete(product)
    db.commit()
    return 'Продукт успешно удален'


@router.put("/{product_id}")
def update_product(product_id, update_product: Product) -> ResponseProduct:
    db = SessionLocal()
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        return 'Продукт не найден'
    product.name = update_product.name
    product.price = update_product.price
    product.description = update_product.description
    db.commit()
    db.refresh(product)
    return product
