class Product:
    def __init__(self, id: int, user_id: int,  name: str, price: float, available_stock: int, colour: str):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.price = price
        self.available_stock = available_stock
        self.colour = colour

    def show_products(self)->str:
        return f"Product id: {self.id}, name: {self.name}, price: {self.price}, total available pieces: {self.available_stock}, colour: {self.colour}."
