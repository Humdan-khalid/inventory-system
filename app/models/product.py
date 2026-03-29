from sqlmodel import SQLModel, Field
from pydantic import BaseModel


class Products(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    name: str = Field(min_length=3, max_length=30)
    brand: str = Field(min_length=2, max_length=30)
    price: float
    available_stock: int = Field(ge=10, le=100000)
    colour: str

class CreateProduct(BaseModel):
    user_id: int
    name: str = Field(min_length=3, max_length=30)
    brand: str = Field(min_length=2, max_length=30)
    price: float
    available_stock:int = Field(ge=10, le=100000)
    colour: str