from typing import List

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from fastAPI.app.src.database import Base, engine
from fastAPI.app.src.dependancies import get_db
from fastAPI.app.src.domain.items.service import get_item as get_item_service
from fastAPI.app.src.domain.items.models import Items
from fastAPI.app.src.domain.items.schemas import *

app = FastAPI()


@app.get("/items")
async def get_items(skip: int = 0, limit: int = 100):
    return {}


@app.get("/items/{item_id}")
async def get_item(item_id: int, db: Session = Depends(get_db)):
    item =  get_item_service(db, item_id= item_id)
    print(item)
    return item


@app.put("/items/create_item")
async def create_item(item: Item):
    return {}


Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
