from sqlalchemy import Column, Integer, String, Float
from ...database import Base


class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    tax = Column(Float)
    units_left = Column(Integer)