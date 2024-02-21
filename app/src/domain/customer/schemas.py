from pydantic import BaseModel


class CustomerBase(BaseModel):
    email_id : str
    user_name: str
    first_name: str
    middle_name: str
    last_name: str
    phone_no: str
    password: str
