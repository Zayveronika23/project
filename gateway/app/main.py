from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/{id}")
def get_product_from_catalog(product_id: int):
    response = requests.get(f"http://catalog:8000/catalog/{product_id}")
    if response.status_code == 200:
        return response.json()
    return 'Продукт не найден'


@app.get("/api/{service}")
def get_list_request(service):
    response = requests.get(url=f"http://{service}:8000/{service}")
    return response.json()


@app.get("/api/{service}/{id}")
def get_request(service, id):
    response = requests.get(url=f"http://{service}:8000/{service}/{id}")
    return response.json()


@app.post("/api/{service}")
def post_request(service, data: dict):
    if service == 'orders':
        order_items_list = []
        for product in data["products"]:
            product_data = get_product_from_catalog(product["product_id"])
            order_items_list.append(
                {"product_id": product_data["id"],
                 "name": product_data["name"],
                 "price": product_data["price"],
                 "quantity": product["quantity"]}
            )
        data = {"order_items": order_items_list}
    response = requests.post(url=f"http://{service}:8000/{service}", json=data)
    return response.json()


@app.delete("/api/{service}/{id}")
def delete_request(service, id):
    response = requests.delete(url=f"http://{service}:8000/{service}/{id}")
    return response.json()


@app.put("/api/{service}/{id}")
def update_request(service, id, data: dict):
    if service == 'orders':
        order_items_list = []
        for product in data["products"]:
            product_data = get_product_from_catalog(product["product_id"])
            order_items_list.append(
                {"product_id": product_data["id"],
                 "name": product_data["name"],
                 "price": product_data["price"],
                 "quantity": product["quantity"]}
            )
        data = {"order_items": order_items_list}
    response = requests.put(url=f"http://{service}:8000/{service}/{id}", json=data)
    return response.json()

@app.get("/health")
def read_root():
    return {"message": "Cateway Service"}