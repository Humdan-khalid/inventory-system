from models.user import User
from models.product import Product
from managers.inventory_manager import InventoryManager
from managers.user_manager import UsersManager
from datetime import datetime

user1 = User(1, "Hamdan", "26-feb-2006", "03190287474", "hamdankhalid111@gmail.com", "Hello273$!", datetime.now())
user2 = User(2, "Emaan", "2-oct-2018", "031846454666", "hamdankhalid111@gmail.com", "Hello273$!", datetime.now())
user3 = User(3, "Muhammad Ibrahim", "9-jun-2014", "03262535353", "muhammadibrahim234@gmail.com", "Youngs255$!", datetime.now())


user_manager = UsersManager([user1])

print(user1.created_at)
print(user_manager.add_user(user2))
print(user_manager.add_user(user3))
user_manager.show_users()





p1 = Product(1, 2, "watch", 1200, 20, "Black")
p2 = Product(2, 1, "Shoes", 2000, 10, "White")
p3 = Product(3, 2, "Perfume", 1500, 8, "Grey")


inventory1 = InventoryManager([p1, p2])


inventory1.add_products(p3)
inventory1.show_all_products(2)
