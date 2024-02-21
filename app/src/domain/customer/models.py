from sqlalchemy import Column, String

from fastAPI.app.src.database import Base


class Customer(Base):
    __tablename__ = "customer"

    email_id = Column(String, primary_key = True, index = True)
    user_name = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    phone_no = Column(String)
    password = Column(String)