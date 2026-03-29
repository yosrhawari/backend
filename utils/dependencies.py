from fastapi import Depends, HTTPException,Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from jose import jwt

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

oauth2_scheme = HTTPBearer()

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")