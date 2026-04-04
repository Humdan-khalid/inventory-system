from fastapi import FastAPI, status, Depends
from app.database.database_connection import get_session
from app.managers.inventory_manager import InventoryManager, Session, CreateProduct
from app.managers.user_manager import CreateUser, UsersManager, LoginUser
from app.utils.jwt import decode_token

app = FastAPI()

@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_products_api(product: CreateProduct, user_token: dict = Depends(decode_token), session: Session = Depends(get_session)):
    manager = InventoryManager()
    return manager.add_products(product, user_token, session)

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user_api(user: CreateUser, session: Session = Depends(get_session)):
    manager = UsersManager()
    return manager.add_user(user, session)

@app.get("/products", status_code=status.HTTP_200_OK)
def get_products_api(user_token: dict = Depends(decode_token), session: Session = Depends(get_session)):
    manager = InventoryManager()
    return manager.show_all_products(user_token, session)

@app.get("/product", status_code=status.HTTP_200_OK)
def get_single_product_api(product_id: int, user_token: dict = Depends(decode_token), session: Session = Depends(get_session)):
    manager = InventoryManager()
    return manager.search_product(product_id, user_token, session)

@app.patch("/stock_update", status_code=status.HTTP_200_OK)
def stock_update_api(product_id: int, stock_quantity: int, user_token: dict = Depends(decode_token), session: Session = Depends(get_session)):
    manager = InventoryManager()
    return manager.update_stock_data(product_id, stock_quantity, user_token, session)

@app.delete("/product_delete", status_code=status.HTTP_200_OK)
def delete_product_api(product_id: int, user_token: dict = Depends(decode_token), session: Session = Depends(get_session)):
    manager = InventoryManager()
    return manager.delete_product(product_id, user_token, session)

@app.post("/login", status_code=status.HTTP_200_OK)
def user_login_api(user: LoginUser, session: Session=Depends(get_session)):
    manager = UsersManager()
    return manager.user_login(user, session)