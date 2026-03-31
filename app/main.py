from fastapi import FastAPI, status, Depends
from app.database.database_connection import get_session
from app.managers.inventory_manager import InventoryManager, Session, CreateProduct
from app.managers.user_manager import CreateUser, UsersManager, LoginUser
from app.utils.jwt import decode_token

app = FastAPI()

@app.post("/products", status_code=status.HTTP_201_CREATED)
def add_products_api(product: CreateProduct, session: Session = Depends(get_session)):
    manager = InventoryManager()
    return manager.add_products(product, session)

@app.post("/users", status_code=status.HTTP_201_CREATED)
def add_user_api(user: CreateUser, session: Session = Depends(get_session)):
    manager = UsersManager()
    return manager.add_user(user, session)

@app.get("/products", status_code=status.HTTP_200_OK)
def get_products(user_token: dict = Depends(decode_token), session: Session = Depends(get_session)):
    manager = InventoryManager()
    return manager.show_all_products(user_token, session)

@app.get("/product", status_code=status.HTTP_200_OK)
def get_product(product_id: int, session: Session = Depends(get_session)):
    manager = InventoryManager()
    return manager.search_product(product_id, session)

@app.patch("/stock_update", status_code=status.HTTP_200_OK)
def create_stock_update(product_id: int, stock_quantity: int, session: Session = Depends(get_session)):
    manager = InventoryManager()
    return manager.update_stock_data(product_id, stock_quantity, session)

@app.delete("/product_delete", status_code=status.HTTP_200_OK)
def delete_product(product_id: int, session: Session = Depends(get_session)):
    manager = InventoryManager()
    return manager.delete_product(product_id, session)

@app.post("/login", status_code=status.HTTP_200_OK)
def user_login(user: LoginUser, session: Session=Depends(get_session)):
    manager = UsersManager()
    return manager.user_login(user, session)