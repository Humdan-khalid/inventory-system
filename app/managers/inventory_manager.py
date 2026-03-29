from app.models.product import CreateProduct, Products
from sqlmodel import Session

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

    # def show_all_products(self, user_id: int):
    #   for product in self.product_list:
    #     if user_id == product.user_id:
    #       print(product.show_products())
      

    # def search_product(self, product_id: int)->str:
    #     try:
    #       product_id = int(product_id)
    #     except ValueError:
    #       return "Invalid input! product_id must be an integer."

    #     if product_id <= 0:
    #       return "Invalid product_id!"

    #     for product in self.product_list:
    #         if product.id == product_id:
    #             return f"Product id: {product.id}, name: {product.name}, price: {product.price}, total available pieces: {product.available_stock}, colour: {product.colour}."
    #     else:
    #         return "Product not found!"

    # def update_data(self, product_id: int)->str:
    #     try:
    #       product_id = int(product_id)
    #     except ValueError:
    #       return "Invalid input! product_id must be an integer."

    #     if product_id <= 0:
    #       return "Invalid product_id!"

    #     for product in self.product_list:
    #         if product.id == product_id:
    #             try:
    #                 new_stock: int = int(input("Enter new stock: "))
    #                 if new_stock <= 0:
    #                   return "Invalid number!"
    #                 product.available_stock += new_stock
    #             except ValueError:
    #                 return "Invalid Value!"
    #             return f"Successfully {new_stock} pieces add in stocks."
    #     else:
    #         return "id not found!"

    # def delete_product(self, product_id: int)->str:
    #     try:
    #       product_id = int(product_id)
    #     except ValueError:
    #       return "Invalid input! product_id must be an integer."

    #     if product_id <= 0:
    #       return "Invalid product_id"

    #     for product in self.product_list:
    #         if product.id == product_id:
    #             self.product_list.remove(product)
    #             return f"product_id: {product_id} successfully deleted."
    #     else:
    #         return "Product not found!"