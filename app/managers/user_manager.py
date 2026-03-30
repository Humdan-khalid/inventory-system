from app.models.user import Users, CreateUser, LoginUser
from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.utils.password_hashing import create_hash_password, verify_password
from app.utils.jwt import create_token, verify_token

class UsersManager:
  def add_user(self, user: CreateUser, session: Session):
    new_user = Users(
      name = user.name.capitalize(),
      date_of_birth = user.date_of_birth,
      phone_number = user.phone_number,
      email = user.email.lower(),
      password = create_hash_password(user.password)
    )

    db_email = session.exec(select(Users).where(Users.email == new_user.email)).first()

    if db_email:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already exist.")

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return{"message": "new user created successfully!"}

  def user_login(self, user: LoginUser, session: Session):
    db_user = session.exec(select(Users).where(Users.email == user.email)).first()
    if not db_user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid email or password!")
    
    if not verify_password(user.password, db_user.password):
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password!")  
      
    new_token = create_token(
      {
        "id": db_user.id,
        "email": db_user.email
      }
      )
    return{
      "access_token": new_token,
      "token_type": "Bearer"
    }
        
  def show_users(self, session: Session):
    db_users = session.exec(select(Users)).all()

    if not db_users:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found!")
    
    return db_users