from jose import jwt
from fastapi import HTTPException
from datetime import datetime, timedelta

from core.models.user import User

def generate_access_token(user: User) -> str:
    expire = datetime.now() + timedelta(minutes=30)
    to_encode = {
                    'email': user.email,
                    'exp': int(expire.strftime('%s'))
                }
    encode_jwt = jwt.encode(to_encode, '896FADCE67C42E186A75D6D6F63FD', 'HS256')
    return encode_jwt


def check_valid_token(access_token: str):
    try:
        payload = jwt.decode(access_token, '896FADCE67C42E186A75D6D6F63FD', 'HS256')
    except:
        raise HTTPException(status_code=403, detail=f"Access token is not valid")
    
    time_now = int(datetime.now().strftime('%s'))
    if time_now > payload:
        raise HTTPException(status_code=403, detail=f"Access token is dead")

