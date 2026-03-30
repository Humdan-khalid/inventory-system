from jose import jwt, ExpiredSignatureError, JWTError
from dotenv import load_dotenv
import os
from datetime import datetime, timezone, timedelta

load_dotenv()

SECRET_KEY = os.getenv("secret_key")
ALGORITHM = os.getenv("algorithm")

def create_token(user_data: dict, exp_time: timedelta = timedelta(minutes=20)):
    if not user_data:
        return "user_data not found!"
    payload = user_data.copy()
    payload["exp"] = datetime.now(timezone.utc) + exp_time

    token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return token

def verify_token(token):
    try:
        token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
        return "Token has expired!"
    except JWTError:
        return "Jwt error!"    
    return token
