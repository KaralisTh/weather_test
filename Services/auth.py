from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    valid_token = os.getenv('AUTH_TOKEN')
    if token != valid_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"token": token}
