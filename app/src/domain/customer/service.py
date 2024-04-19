import datetime
import os

import bcrypt
from fastapi import HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastAPI.app.src.domain.customer.models import Customer
from fastAPI.app.src.domain.customer.schemas import CustomerBase
import jwt
from jwt import PyJWTError

SECRET_KEY = "abcd"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20


def get_customer_service(db: Session, email_id: str):
    return db.query(Customer).filter(Customer.email_id == email_id).first()


def get_customers_service(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()


def create_customer_service(db: Session, customer=CustomerBase):
    customer_dict = customer.dict()
    customer_dict['hashed_password'] = bcrypt.hashpw(customer.password.encode('utf-8'), bcrypt.gensalt(6))
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
    is_validated_customer = bcrypt.checkpw(password.encode('utf-8'), hashed_pwd)
    return is_validated_customer


def create_access_token(data: dict, expires_delta):
    to_encode = data
    expire = datetime.datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_access_token(data: dict):
    expires_delta = datetime.timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data,expires_delta)
    return access_token


def authenticate(self, token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        print("payload: ", payload)
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Authentication failed, invalid or expired token")
