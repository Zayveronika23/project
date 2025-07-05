from fastapi import FastAPI
from ..db.db import Base, engine
from sqlalchemy.orm import sessionmaker
from ..db.models import OrderModel, OrderItemModel
from ..schemas.schemas import Order, OrderItem
from fastapi import APIRouter

router = APIRouter()


Base.metadata.create_all(bind=engine)

app = FastAPI()


SessionLocal = sessionmaker(autoflush=False, bind=engine)

router = APIRouter()

@router.get("/{order_id}")
def get_order(order_id) -> Order:
    db = SessionLocal()
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not order:
        return 'Заказ не найден'
    return order


@router.get("/")
def get_orders() -> list[Order]:
    db = SessionLocal()
    return db.query(OrderModel).all()


@router.post("/")
def create_order(order: Order) -> Order:
    db = SessionLocal()
    new_order = OrderModel(
        total_cost=order.total_cost,
        created_at=order.created_at
    )
    for order_item in order.order_items:
        new_order_item = OrderItemModel(
            quantity=order_item.quantity,
            product_id=order_item.product_id,
            name=order_item.name,
            price=order_item.price
        )
        new_order.order_items.append(new_order_item)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.delete("/{order_id}")
def delete_order(order_id):
    db = SessionLocal()
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not order:
        return 'Заказ не найден'
    db.delete(order)
    db.commit()
    return 'Заказ успешно удален'


@router.put("/{order_id}")
def update_order(order_id, update_order: Order) -> Order:
    db = SessionLocal()
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not order:
        return 'Заказ не найден'
    order.total_cost = update_order.total_cost
    db.query(OrderItemModel).filter(OrderItemModel.order_id == order_id).delete()
    for order_item in update_order.order_items:
        update_order_item = OrderItemModel(
            quantity=order_item.quantity,
            product_id=order_item.product_id,
            name=order_item.name,
            price=order_item.price
        )
        order.order_items.append(update_order_item)
    db.commit()
    db.refresh(order)
    return order