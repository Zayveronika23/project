# Сервис для управления каталогом и заказами.           

### Краткое описание:
Сервис для управления сервисом заказов и сервисом каталога

### Сборка и запуск:

```bash
Клонируем 3 репозитория
git clone git@github.com:Zayveronika23/catalog_service.git
git clone git@github.com:Zayveronika23/order_service.git
git clone git@github.com:Zayveronika23/gateway_service.git

Переходим в директорию:
cd gateway_service

Запускаем проект:
* export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin/"
docker-compose up --build     
```
### Примеры запросов:
* GET запрос к http://0.0.0.0:8000/api/catalog/ - для получения каталога товаров  
  GET запрос к http://0.0.0.0:8000/api/orders/ - для получения списка заказов

* GET запрос к http://0.0.0.0:8000/api/catalog/<id> - для получения товара  
  GET запрос к http://0.0.0.0:8000/api/orders/<id> - для получения заказа

* POST запрос к http://0.0.0.0:8000/api/catalog/ - для создания товара  
{
   "name": "Название товара",  
   "price": 100,  
   "description": "Описание"}  
POST запрос к http://0.0.0.0:8000/api/orders/- для создания заказа  
{
    "products": [  
        { "product_id": 1,  
          "quantity": 1 } ]  
}  

* PUT запрос к http://0.0.0.0:8000/api/catalog/<id> - для изменения товара  
{  
   "name": "Новое название товара",  
   "price": 200,  
   "description": "Новое описание"  
}  
  PUT запрос к http://0.0.0.0:8000/api/orders/<id> - для изменения заказа  
{  
    "products": [  
        {  
            "product_id": 2,  
            "quantity": 2  
        }  
    ]  
}  

* DELETE запрос к http://0.0.0.0:8000/api/catalog/<id> - для удаления товара  
  DELETE запрос к http://0.0.0.0:8000/api/orders/<id> - для удаления заказа
  

