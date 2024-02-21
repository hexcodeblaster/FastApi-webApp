from typing import List

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from fastAPI.app.src.database import Base, engine
from fastAPI.app.src.dependancies import get_db
from fastAPI.app.src.domain.customer.models import Customer
from fastAPI.app.src.domain.customer.schemas import CustomerBase
from fastAPI.app.src.domain.items.service import get_item as get_item_service, \
    get_items as get_items_service, \
    create_item as create_item_service, \
    delete_item as delete_item_service
from fastAPI.app.src.domain.customer.service import get_customer as get_customer_service, \
    get_customers as get_customers_service, \
    create_customer as create_customer_service, \
    delete_customer as delete_customer_service
from fastAPI.app.src.domain.items.models import Items
from fastAPI.app.src.domain.items.schemas import *

app = FastAPI()


@app.get("/items")
async def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items_service(db, skip=skip, limit=limit)
    return items


@app.get("/items/{item_id}")
async def get_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item_service(db, item_id=item_id)
    return item


@app.put("/items/create_item")
async def create_item(item: Item, db: Session = Depends(get_db)):
    return create_item_service(db=db, item=item)


@app.delete("/items/delete_item")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    return delete_item_service(db=db, item_id=item_id)


@app.get("/customer")
async def get_customers(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_customers_service(db=db, skip=skip, limit=limit)


@app.get("/customer/{email_id}")
async def get_customer(email_id: str, db: Session = Depends(get_db)):
    return get_customer_service(db=db, email_id=email_id)


@app.put("/customer/create_customer")
async def create_customer(customer: CustomerBase, db: Session = Depends(get_db)):
    return create_customer_service(db=db, customer=customer)


@app.delete("/customer/delete_customer")
async def delete_customer(email_id: str, db: Session = Depends(get_db)):
    delete_customer_service(db=db, email_id=email_id)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
