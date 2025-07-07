from fastapi import FastAPI
from .db import models, db
from .api import products

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

app.include_router(products.router, prefix="/catalog", tags=["products"])

@app.get("/health")
def read_root():
    return {"message": "Catalog Service"}