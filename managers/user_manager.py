from models.user import User

class UsersManager:
  def __init__(self, users_list: list):
    self.users_list = users_list

  def add_user(self, customer: User):
    self.users_list.append(customer)
    return f"{customer.name} successfully add in list."

  def show_users(self):
    for user in self.users_list:
      print(user.show_users())