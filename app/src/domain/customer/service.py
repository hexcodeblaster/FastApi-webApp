import bcrypt
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastAPI.app.src.domain.customer.models import Customer
from fastAPI.app.src.domain.customer.schemas import CustomerBase


def get_customer_service(db: Session, email_id: str):
    return db.query(Customer).filter(Customer.email_id == email_id).first()


def get_customers_service(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()


def create_customer_service(db: Session, customer=CustomerBase):
    customer_dict = customer.dict()
    customer_dict['hashed_password'] = bcrypt.hashpw(customer.password.encode('utf-8'), bcrypt.gensalt(6))
    print(customer_dict['hashed_password'])
    customer_dict.pop('password')
    new_customer = Customer(**customer_dict)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


def delete_customer_service(db: Session, email_id: str):
    db.query(Customer).filter(Customer.email_id == email_id).delete()
    db.commit()


def validate_customer_service(db: Session, email_id: str, password: str):
    customer = get_customer_service(db, email_id=email_id)
    hashed_pwd = customer.__dict__.get('hashed_password')
    return bcrypt.checkpw(password.encode('utf-8'), hashed_pwd)

