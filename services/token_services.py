from jose import jwt
import os 
from fastapi import HTTPException
from datetime import datetime, timedelta

from core.models.user import User

def generate_access_token(user: User) -> str:
    expire = datetime.now() + timedelta(minutes=30)
    to_encode = {
                    'email': user.email,
                    'exp': int(expire.strftime('%s'))
                }
    encode_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), os.getenv('ALGORITM_HASHING'))
    return encode_jwt


def check_valid_token(access_token: str):
    try:
        payload = jwt.decode(access_token, os.getenv('SECRET_KEY'), os.getenv('ALGORITM_HASHING'))
    except:
        raise HTTPException(status_code=403, detail=f"Access token is not valid")
    
    time_now = int(datetime.now().strftime('%s'))
    if time_now > payload['exp']:
        raise HTTPException(status_code=403, detail=f"Access token is dead")

