from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
    tax: float
    units_left: int

    class Config:
        orm_mode = True