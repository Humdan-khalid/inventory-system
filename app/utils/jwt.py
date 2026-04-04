from jose import jwt, ExpiredSignatureError, JWTError
from dotenv import load_dotenv
import os
from datetime import datetime, timezone, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

SECRET_KEY = os.getenv("secret_key")
ALGORITHM = os.getenv("algorithm")

def create_token(user_data: dict, exp_time: timedelta = timedelta(minutes=20)):
    if not user_data:
        raise TypeError("user_data not found!")
    payload = user_data.copy()
    payload["exp"] = datetime.now(timezone.utc) + exp_time

    token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return token

def verify_token(token):
    try:
        token_decode = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired!")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="jwt error!")    
    return token_decode

security = HTTPBearer()

def decode_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    return verify_token(token)
