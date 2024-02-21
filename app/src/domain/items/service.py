from sqlalchemy.orm import Session
from .models import Items
from .schemas import Item as Item_schema


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Items).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.query(Items).filter(Items.id == item_id).all()


def create_item(db: Session, item: Item_schema):
    item_new = Items(**item.dict())
    db.add(item_new)
    db.commit()
    db.refresh(item_new)
    return item_new


def delete_item(db: Session, item_id: int):
    return db.query(Items).filter(Items.id == item_id).delete()
