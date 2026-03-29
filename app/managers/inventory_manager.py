from app.models.product import CreateProduct, Products
from sqlmodel import Session, select
from fastapi import HTTPException, status

class InventoryManager:
    def add_products(self, product: CreateProduct, session: Session)->str:
      new_product = Products(
        user_id = product.user_id,
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

    def show_all_products(self, user_id: int, session: Session):
        db_products = session.exec(select(Products).where(Products.user_id == user_id)).all()

        if not db_products:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Products not found!")
        
        return {"Products": db_products}
      

    def search_product(self, product_id: int, session: Session)->str:
        db_product = session.exec(select(Products).where(Products.id == product_id)).first()

        if not db_product:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found!")
        
        return db_product

    def update_stock_data(self, product_id: int, stock_quantity: int, session: Session)->str:
      if product_id <= 0:
        return "Invalid product_id!"
      
      db_product = session.exec(select(Products).where(Products.id == product_id)).first()
      
      if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found!")

      if stock_quantity <= 0:
        return "Invalid stock quantity!"
      
      db_product.available_stock += stock_quantity

      session.add(db_product)
      session.commit()

      return{"message": f"Successfully add {stock_quantity} pieces in stock."}
      

    def delete_product(self, product_id: int, session: Session)->str:
        if product_id <= 0:
          return "Invalid product_id"
        
        db_product = session.exec(select(Products).where(Products.id == product_id)).first()

        if not db_product:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found!")

        session.delete(db_product)
        session.commit()

        return {"Message": "product deleted successfully."}