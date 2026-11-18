from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
password_hash = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    hash = password_hash.hash(password)

    return hash

def verify_hash(password: str, db_hash: str) -> bool:
    return password_hash.verify(db_hash, get_password_hash(password))

def get_oauth2_scheme():
    return oauth2_scheme