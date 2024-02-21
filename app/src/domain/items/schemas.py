from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
    tax: float | None = None
    units_left: int | None = None

    class Config:
        orm_mode = True