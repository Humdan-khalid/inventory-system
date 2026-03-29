from sqlmodel import SQLModel, Field
from pydantic import EmailStr, BaseModel

class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=40)
    date_of_birth: str
    phone_number: str = Field(min_length=11, max_length=11, unique=True)
    email: EmailStr = Field(index=True, unique=True)
    password: str = Field(min_length=6, max_length=30)

class CreateUser(BaseModel):
    name: str = Field(min_length=3, max_length=40)
    date_of_birth: str
    phone_number: str = Field(min_length=11, max_length=11, unique=True)
    email: EmailStr = Field(index=True, unique=True)
    password: str = Field(min_length=6, max_length=30)