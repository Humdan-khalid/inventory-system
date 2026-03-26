from sqlmodel import SQLModel, Field
from pydantic import EmailStr, BaseModel

class Users(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    date_of_birth: str = Field(nullable=False)
    phone_number: str = Field(nullable=False, unique=True)
    email: EmailStr = Field(nullable=False, index=True, unique=True)
    password: str = Field(nullable=False)

class CreateUser(BaseModel):
    name: str
    date_of_birth: str
    phone_number: str
    email: EmailStr
    password: str


class Products(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    name: str = Field(nullable=False)
    brand: str = Field(nullable=False)
    price: float = Field(nullable=False)
    available_stock: int = Field(nullable=False)
    colour: str = Field(nullable=False)

class CreateProduct(BaseModel):
    name: str
    brand: str
    price: float
    available_stock: int
    colour: str