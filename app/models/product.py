from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel
from app.models.user import Users
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import Users

class Products(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    name: str = Field(min_length=3, max_length=30)
    brand: str = Field(min_length=2, max_length=30)
    price: float
    available_stock: int = Field(ge=10, le=100000)
    colour: str

    user: "Users" = Relationship(back_populates="products")

class CreateProduct(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    brand: str = Field(min_length=2, max_length=30)
    price: float
    available_stock:int = Field(ge=10, le=100000)
    colour: str