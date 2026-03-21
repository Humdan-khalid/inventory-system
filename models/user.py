from datetime import datetime

class User:
  def __init__(self, id: int, name: str, date_of_birth: str, phone_number: str, email: str, password, created_at: datetime):
    self.id = id
    self.name = name
    self.date_of_birth = date_of_birth
    self.phone_number = phone_number
    self.email = email
    self.password = password
    self.created_at = created_at

  def show_users(self)->str:
    return f"id: {self.id}, name: {self.name}, date_of_birth: {self.date_of_birth}, email: {self.email}."
