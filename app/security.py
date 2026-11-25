from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
import jwt
from app.schemas.schemas import TokenData, Token
from jwt.exceptions import InvalidTokenError
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import UTC, datetime, timedelta
from app.dependencies import get_data_manager
from typing import Annotated

data_manager = get_data_manager()
password_hash = PasswordHash.recommended()
DUMMY_HASH = password_hash.hash("eewrwiiIIuuer")

def get_password_hash(password: str) -> str:
    hash = password_hash.hash(password)

    return hash

def verify_hash(password: str, db_hash: str) -> bool:
    return password_hash.verify(db_hash, get_password_hash(password))

def get_oauth2_scheme():
    
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    return oauth2_scheme


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(username: str, password: str):
    user = data_manager.get_user(username)
    if not user:
        verify_hash(password, DUMMY_HASH)
        return False
    if not verify_hash(password, user["password_hash"]):
        return False
    return user

async def get_current_user(token: Annotated[str, Depends(get_oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}, 
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None :
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = data_manager.get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user



