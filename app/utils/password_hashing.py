from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated = "auto",
    bcrypt__rounds = 10
)

def create_hash_password(user_password: str)->str:
    if not user_password:
        raise ValueError("User passwoord is None.")
    hash_password = pwd_context.hash(user_password)
    return hash_password

def verify_password(user_password: str, hashed_password: str):
    if not user_password:
        raise ValueError("User password is None!")
    if not hashed_password:
        raise ValueError("hashed password is None!")
    
    password_verify = pwd_context.verify(user_password, hashed_password)
    return password_verify