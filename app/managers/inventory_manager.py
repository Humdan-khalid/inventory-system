from app.models.product import CreateProduct
from sqlmodel import Session, select
from fastapi import HTTPException, status                                                                                                                                                                                                                                   
from app.models.user import Users
from app.models.product import Products

class InventoryManager:
    def add_products(self, product: CreateProduct, user_token: dict, session: Session):
      db_user = session.exec(select(Users).where(Users.id == user_token["id"])).first()
      
      new_product = Products(
        user_id = db_user.id,
        name = product.name,
        brand = product.brand,
        price = product.price,
        available_stock=product.available_stock,
        colour=product.colour
        )
      
      session.add(new_product)
      session.commit()
      session.refresh(new_product)
      
      return "Product successfully save."

    def show_all_products(self, user_token: dict, session: Session):
        db_products = session.exec(select(Products).where(Products.user_id == user_token["id"])).all()

        if not db_products:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Products not found!")
        
        return {"Products": db_products}
      

    def search_product(self, product_id: int, user_token: dict, session: Session):
        db_product = session.exec(select(Products).where(Products.id == product_id)).first()

        if not db_product:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found!")
        
        if db_product.user_id != user_token["id"]:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user!")
           
        return db_product

    def update_stock_data(self, product_id: int, stock_quantity: int, user_token: dict, session: Session):
      if product_id <= 0:
        return "Invalid product_id!"

      if stock_quantity <= 0:
        return "Invalid stock quantity!"
        
      db_product = session.exec(select(Products).where(Products.id == product_id)).first()
      
      if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found!")
      
      if db_product.user_id != user_token["id"]:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user!")
      
      db_product.available_stock += stock_quantity

      session.add(db_product)
      session.commit()

      return{"message": f"Successfully add {stock_quantity} pieces in stock."}
      

    def delete_product(self, product_id: int, user_token: dict, session: Session)->str:
        if product_id <= 0:
          return "Invalid product_id"
        
        db_product = session.exec(select(Products).where(Products.id == product_id)).first()

        if not db_product:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found!")
        
        if db_product.user_id != user_token["id"]:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user!")

        session.delete(db_product)
        session.commit()

        return {"Message": "product deleted successfully."}