from sqlalchemy import Column, String, LargeBinary

from fastAPI.app.src.database import Base


class Customer(Base):
    __tablename__ = "customer"

    email_id = Column(String, primary_key = True, index = True)
    user_name = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    phone_no = Column(String)
    hashed_password = Column(LargeBinary)

    def __str__(self):
        return ", ".join(self.__dir__())
