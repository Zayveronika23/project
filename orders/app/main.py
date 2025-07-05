from fastapi import FastAPI
from .db import models, db
from .api import orders

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

app.include_router(orders.router, prefix="/orders", tags=["orders"])


@app.get("/health")
def read_root():
    return {"message": "Order Service"}