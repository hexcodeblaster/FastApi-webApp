from sqlalchemy.orm import Session

from fastAPI.app.src.domain.customer.models import Customer
from fastAPI.app.src.domain.customer.schemas import CustomerBase


def get_customer(db: Session, email_id: str):
    return db.query(Customer).filter(Customer.email_id == email_id).all()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()


def create_customer(db: Session, customer=CustomerBase):
    new_customer = Customer(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


def delete_customer(db: Session, email_id: str):
    db.query(Customer).filter(Customer.email_id == email_id).delete()
    db.commit()
