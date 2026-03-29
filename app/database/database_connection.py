import os
from dotenv import load_dotenv
from sqlmodel import create_engine
from sqlmodel import Session

load_dotenv()

database_url = os.getenv("database_url")

if not database_url:
    raise ValueError("datbase_url not found!")

engine = create_engine(
    database_url,
    echo = True,
    pool_size=10,
    max_overflow=20,
    future=True
)

def get_session():
    with Session(engine) as session:
        yield session


